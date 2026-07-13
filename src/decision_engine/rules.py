"""
Rule-based decision configurations.
"""
class ExpertRulesEngine:
    """Evaluates logic rules from agronomist profiles."""
    
    def evaluate_rules(self, crop: str, stage: str, sensor_values: dict) -> list:
        """Return list of rules violated."""
        return []
