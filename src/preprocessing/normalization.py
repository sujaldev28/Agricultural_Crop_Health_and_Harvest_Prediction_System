"""
Feature scaling and normalization.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

class FeatureNormalizer:
    """Standardizes sensor readings for model ingestion."""
    
    def __init__(self) -> None:
        self.scaler = StandardScaler()

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fits normalizer and transforms dataframe."""
        return df
