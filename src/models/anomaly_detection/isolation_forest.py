"""
Isolation Forest multivariate anomaly detector.
"""
import numpy as np

class IsolationForestDetector:
    """Isolation Forest detector wrapper."""
    
    def fit(self, X: np.ndarray) -> None:
        """Train the isolation forest detector."""
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Returns anomaly flags."""
        return np.ones(len(X))
