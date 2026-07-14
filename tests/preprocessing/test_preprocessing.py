"""
Tests for preprocessing cleaners and imputers.
"""
import pytest
import pandas as pd
from src.preprocessing.cleaning import DataCleaner
from src.preprocessing.missing_values import MissingValueImputer

def test_data_cleaner() -> None:
    cleaner = DataCleaner()
    df = pd.DataFrame({"sensor_id": [1, None, 3], "timestamp": ["2026-07-13", "2026-07-13", None]})
    cleaned_df = cleaner.clean(df)
    assert len(cleaned_df) == 1

def test_missing_value_imputer() -> None:
    imputer = MissingValueImputer()
    df = pd.DataFrame({"val": [10.0, None, 12.0]})
    imputed = imputer.impute(df, method="ffill")
    assert imputed["val"].iloc[1] == 10.0
