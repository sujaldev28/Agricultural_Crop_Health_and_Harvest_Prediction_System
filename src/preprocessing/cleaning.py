"""
Raw data cleaning utilities.
"""
import pandas as pd

class DataCleaner:
    """Removes invalid, corrupt, or malformed values."""
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Cleans the dataframe based on range limits."""
        # TODO: Add cleaning rules
        return df.dropna(subset=['sensor_id', 'timestamp'])
