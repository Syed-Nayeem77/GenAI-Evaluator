import logging
import joblib
from pathlib import Path
from typing import Dict, Any, Optional
import numpy as np
from .metrics import EvaluationMetrics

logger = logging.getLogger(__name__)

class Evaluator:
    """Main evaluation engine"""
    
    def __init__(self, model_path: Path):
        try:
            self.model = joblib.load(model_path)
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise
    
    def evaluate(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate model outputs"""
        try:
            # Example evaluation flow
            predictions = self.model.predict([inputs['text']])
            metrics = EvaluationMetrics.calculate_classification_metrics(
                np.array([inputs['label']]),
                predictions
            )
            return {
                'prediction': predictions[0],
                'metrics': metrics
            }
        except Exception as e:
            logger.error(f"Evaluation failed: {str(e)}")
            raise
