"""
Export trained models to registry format (ONNX, joblib, etc.).
"""
import logging
from src.common.logger import setup_logger

logger = setup_logger("export_script")

def main() -> None:
    logger.info("Exporting models to production registry...")
    # TODO: Export logic
    logger.info("Model exporting finished.")

if __name__ == "__main__":
    main()
