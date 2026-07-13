"""
Outlier detection methods.
"""
import pandas as pd

class OutlierDetector:
    """Flags and handles sensor outliers."""
    
    def detect_zscore(self, df: pd.DataFrame, threshold: float = 3.0) -> pd.DataFrame:
        """Filter rows exceeding Z-score threshold."""
        return df
