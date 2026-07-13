"""
Integration test tracing ingestion, preprocessing, and features together.
"""
import pytest
import pandas as pd
from src.preprocessing.cleaning import DataCleaner
from src.feature_engineering.gdd import GDDCalculator

def test_pipeline_integration() -> None:
    df = pd.DataFrame({"sensor_id": ["S1"], "timestamp": ["2026-07-13T12:00:00"]})
    cleaner = DataCleaner()
    cleaned = cleaner.clean(df)
    assert len(cleaned) == 1
    
    gdd = GDDCalculator()
    val = gdd.calculate(25, 15, 10)
    assert val == 10.0
