import joblib
from pathlib import Path
import json
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class ModelLoader:
    """Handles loading of model artifacts"""
    
    def __init__(self, model_dir: Path):
        self.model_dir = model_dir
        self.model = None
        self.tokenizer = None
        self.metadata = None
        self._load_artifacts()
    
    def _load_artifacts(self) -> None:
        """Load all model artifacts"""
        try:
            # Load model
            self.model = joblib.load(self.model_dir / "model.pkl")
            
            # Load tokenizer if exists
            tokenizer_path = self.model_dir / "tokenizer/tokenizer.pkl"
            if tokenizer_path.exists():
                self.tokenizer = joblib.load(tokenizer_path)
            
            # Load metadata
            with open(self.model_dir / "metadata.json") as f:
                self.metadata = json.load(f)
                
            logger.info(f"Successfully loaded model version {self.metadata['model_version']}")
            
        except Exception as e:
            logger.error(f"Failed to load model artifacts: {str(e)}")
            raise RuntimeError("Model loading failed") from e

    def get_input_schema(self) -> Dict[str, Any]:
        """Get expected input schema"""
        return self.metadata.get("input_schema", {})
    
    def get_output_schema(self) -> Dict[str, Any]:
        """Get expected output schema"""
        return self.metadata.get("output_schema", {})
