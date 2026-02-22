from typing import Any


def predict_sentiment(text: str, pipeline: Any) -> int:
    """Run minimal preprocessing and return sentiment label (0/1)."""
    cleaned_text = text.strip()
    if len(cleaned_text) < 3:
        raise ValueError("Input text must have at least 3 characters after trimming.")

    prediction = pipeline.predict([cleaned_text])
    return int(prediction[0])
