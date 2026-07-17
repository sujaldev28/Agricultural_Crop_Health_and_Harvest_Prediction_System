"""
FastAPI Main Application entrypoint.
"""
from fastapi import FastAPI
from src.common.constants import PROJECT_NAME

app = FastAPI(title=PROJECT_NAME, version="1.0.0")

@app.get("/health")
def health_check():
    """Liveness and readiness check."""
    
    return {"status": "healthy", "service": PROJECT_NAME}
