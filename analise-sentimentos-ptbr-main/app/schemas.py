from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=3, description="Texto para analise de sentimento")


class PredictResponse(BaseModel):
    label: int
    label_name: str
    input_text: str
