"""
Missing value imputation strategies.
"""
import pandas as pd

class MissingValueImputer:
    """Imputes missing values in timeseries sensor data."""
    
    def impute(self, df: pd.DataFrame, method: str = "interpolate") -> pd.DataFrame:
        """Impute values with selected strategy."""
        if method == "interpolate":
            return df.interpolate(method='linear')
        return df.fillna(method='ffill')
