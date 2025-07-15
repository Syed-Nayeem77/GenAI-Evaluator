from pydantic import BaseSettings
from pathlib import Path
from typing import Optional

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "GenAI-Evaluator"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    # Model
    MODEL_DIR: Path = Path("models/evaluator/latest")
    TOKENIZER_PATH: Path = MODEL_DIR / "tokenizer"
    MODEL_PATH: Path = MODEL_DIR / "model.pkl"
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_WORKERS: int = 2
    
    # Data
    DATA_DIR: Path = Path("data")
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
