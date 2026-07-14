"""
Feature Engineering pipeline manager.
"""
import pandas as pd
from src.feature_engineering.feature_pipeline import FeatureEngineeringPipeline

class PipelineFeatureStore:
    """Calculates all features and prepares dataset matrix."""
    
    def run(self, clean_df: pd.DataFrame) -> pd.DataFrame:
        """Run calculation workflow."""
        pipeline = FeatureEngineeringPipeline()
        return pipeline.transform(clean_df)
