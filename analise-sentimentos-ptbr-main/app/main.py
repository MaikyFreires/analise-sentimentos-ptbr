from pathlib import Path

from fastapi import FastAPI, HTTPException, Response

from .schemas import PredictRequest, PredictResponse
from .services.model_loader import load_pipeline
from .services.predictor import predict_sentiment


app = FastAPI(
    title="Sentiment Analysis API",
    description="MVP academico de analise de sentimentos em PT-BR",
    version="1.0.0",
)

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "sentiment_pipeline.joblib"
PIPELINE = None
LABEL_MAP = {0: "negativo", 1: "positivo"}


@app.on_event("startup")
def startup_event() -> None:
    global PIPELINE
    try:
        PIPELINE = load_pipeline(str(MODEL_PATH))
    except Exception as exc:
        # API remains up for diagnostics, but prediction is blocked until model is available.
        PIPELINE = None
        print(f"[startup] Failed to load model: {exc}")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Sentiment Analysis API running.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> Response:
    return Response(status_code=204)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest) -> PredictResponse:
    if PIPELINE is None:
        raise HTTPException(
            status_code=500,
            detail="Model is not loaded. Run scripts/export_model.py before starting the API.",
        )

    try:
        label = predict_sentiment(payload.text, PIPELINE)
    except ValueError as exc:
        # Defensive validation in service layer.
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Prediction error: {exc}") from exc

    label_name = LABEL_MAP.get(label, "desconhecido")
    return PredictResponse(label=label, label_name=label_name, input_text=payload.text)
