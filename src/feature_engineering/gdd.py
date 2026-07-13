"""
Growing Degree Days (GDD) calculator.
"""
class GDDCalculator:
    """Calculates GDD for crops based on base temperatures."""
    
    def calculate(self, max_temp: float, min_temp: float, base_temp: float) -> float:
        """GDD = ((T_max + T_min) / 2) - T_base"""
        return max(0.0, ((max_temp + min_temp) / 2.0) - base_temp)
