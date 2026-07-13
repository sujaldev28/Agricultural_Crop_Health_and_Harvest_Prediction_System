"""
Feature store loader.
"""
import pandas as pd

class FeatureStoreLoader:
    """Loads train/inference matrices from feature store database."""
    
    def load_features(self, crop_type: str) -> pd.DataFrame:
        """Load crop features."""
        return pd.DataFrame()
