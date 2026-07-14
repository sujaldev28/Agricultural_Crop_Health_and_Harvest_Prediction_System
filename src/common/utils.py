"""
General helper functions.
"""
from datetime import datetime

def parse_iso_timestamp(ts_str: str) -> datetime:
    """Parse ISO timestamp helper."""
    return datetime.fromisoformat(ts_str)
