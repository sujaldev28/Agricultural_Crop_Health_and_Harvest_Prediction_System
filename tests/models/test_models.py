"""
Tests for model placeholder predictions.
"""
import pytest
from src.models.anomaly_detection.zscore import ZScoreAnomalyDetector

def test_zscore_detector() -> None:
    detector = ZScoreAnomalyDetector()
    is_anomaly = detector.predict(val=45.0, mean=20.0, std=5.0, threshold=3.0)
    assert is_anomaly is True
