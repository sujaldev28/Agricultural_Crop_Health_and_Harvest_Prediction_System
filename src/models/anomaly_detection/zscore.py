"""
Z-score based univariate anomaly detection.
"""
class ZScoreAnomalyDetector:
    """Identifies statistical outliers outside threshold bounds."""
    
    def predict(self, val: float, mean: float, std: float, threshold: float = 3.0) -> bool:
        """True if anomaly."""
        if std == 0:
            return False
        return abs(val - mean) / std > threshold
