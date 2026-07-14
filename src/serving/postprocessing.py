"""
Postprocessing of model predictions.
"""
class PostProcessor:
    """Converts classification/regression values to user-facing models."""
    
    def format_predictions(self, raw_pred: dict) -> dict:
        """Return formatted predictions."""
        return raw_pred
