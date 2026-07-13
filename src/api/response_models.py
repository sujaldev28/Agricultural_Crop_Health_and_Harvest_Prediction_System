"""
Pydantic API response model definitions.
"""
from pydantic import BaseModel
from typing import List, Dict

class PredictionResponse(BaseModel):
    status: str
    sensor_id: str
    anomalies: List[str]
    predictions: Dict[str, float]
    recommendations: List[str]
