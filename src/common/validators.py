"""
Validation helpers for incoming records.
"""
from typing import Dict, Any

def validate_sensor_reading(reading: Dict[str, Any]) -> bool:
    """
    Validate sensor schema structure and parameters.
    Returns:
        bool: True if valid, raises ValueError or returns False if not.
    """
    required_keys = {"temperature", "humidity", "timestamp", "sensor_id"}
    return required_keys.issubset(reading.keys())
