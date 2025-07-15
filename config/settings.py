from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "GenAI-Evaluator"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    # Model paths
    MODEL_DIR: Path = Path("models/evaluator/latest")
    TOKENIZER_DIR: Path = MODEL_DIR / "tokenizer"
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_WORKERS: int = 4
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
