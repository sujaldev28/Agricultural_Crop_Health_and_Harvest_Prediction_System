"""
Custom exceptions for the application.
"""
class AgriSystemError(Exception):
    """Base exception for all systems."""
    pass

class DataIngestionError(AgriSystemError):
    """Raised when data ingestion fails."""
    pass

class PreprocessingError(AgriSystemError):
    """Raised when data preprocessing fails."""
    pass

class ModelExecutionError(AgriSystemError):
    """Raised when model inference or training fails."""
    pass
