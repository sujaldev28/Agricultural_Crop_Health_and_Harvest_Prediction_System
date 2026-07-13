"""
Missing value imputation strategies.
"""
import pandas as pd

class MissingValueImputer:
    """Imputes missing values in timeseries sensor data."""
    
    def impute(self, df: pd.DataFrame, method: str = "interpolate") -> pd.DataFrame:
        """Impute missing values in a pandas DataFrame.

        Args:
            df: The input pandas DataFrame with missing values.
            method: The imputation method ('interpolate', 'ffill', 'bfill').

        Returns:
            pd.DataFrame: Imputed DataFrame.
        """
        if method == "interpolate":
            return df.interpolate(method='linear')
        elif method == "ffill":
            return df.ffill()
        elif method == "bfill":
            return df.bfill()
        else:
            raise ValueError(f"Unknown imputation method: {method}")
