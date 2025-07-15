import pytest
from unittest.mock import MagicMock
import numpy as np
from src.evaluation.evaluator import Evaluator

class TestEvaluator:
    @pytest.fixture
    def mock_model(self):
        model = MagicMock()
        model.predict.return_value = np.array([1])
        return model

    def test_evaluate_success(self, mock_model, tmp_path):
        # Create temporary model file
        model_path = tmp_path / "model.pkl"
        import joblib
        joblib.dump(mock_model, model_path)
        
        evaluator = Evaluator(model_path)
        result = evaluator.evaluate({
            "text": "sample text",
            "label": 1
        })
        
        assert "prediction" in result
        assert "metrics" in result
        assert result["prediction"] == 1
        assert "accuracy" in result["metrics"]

    def test_evaluate_failure(self, tmp_path):
        with pytest.raises(Exception):
            Evaluator(tmp_path / "nonexistent.pkl")
