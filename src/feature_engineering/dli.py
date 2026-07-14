"""
Daily Light Integral (DLI) calculator.
"""
class DLICalculator:
    """Calculates DLI based on lux levels over a 24h duration."""
    
    def calculate(self, avg_lux: float, photoperiod_hours: float) -> float:
        """Daily Light Integral calculation."""
        return avg_lux * photoperiod_hours * 0.0079
