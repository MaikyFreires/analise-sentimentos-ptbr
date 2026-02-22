from pathlib import Path
from typing import Any

import joblib


_PIPELINE_CACHE: dict[str, Any] = {}


def load_pipeline(path: str) -> Any:
    """Load and cache a trained sentiment pipeline from disk."""
    if path in _PIPELINE_CACHE:
        return _PIPELINE_CACHE[path]

    pipeline_path = Path(path)
    if not pipeline_path.exists():
        raise FileNotFoundError(f"Pipeline file not found: {pipeline_path}")

    pipeline = joblib.load(pipeline_path)
    _PIPELINE_CACHE[path] = pipeline
    return pipeline
