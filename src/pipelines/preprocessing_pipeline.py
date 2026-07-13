"""
Data Preprocessing pipeline manager.
"""
import pandas as pd
from src.preprocessing.cleaning import DataCleaner

class PreprocessingPipeline:
    """Runs data clearing, imputation, and normalizing processes."""
    
    def run(self, raw_df: pd.DataFrame) -> pd.DataFrame:
        """Execute preprocessing."""
        cleaner = DataCleaner()
        return cleaner.clean(raw_df)
