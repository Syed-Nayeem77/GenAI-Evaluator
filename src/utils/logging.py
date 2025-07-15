import logging
import logging.config
from pathlib import Path
from config.settings import settings
import os

def setup_logging():
    """Configure logging from file"""
    log_config = Path("config/logging.conf")
    if log_config.exists():
        logging.config.fileConfig(log_config)
    else:
        logging.basicConfig(level=settings.LOG_LEVEL)
    
    # Ensure log directory exists
    os.makedirs("logs", exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    """Get configured logger instance"""
    return logging.getLogger(name)
