import numpy as np
from src.evaluation.metrics import EvaluationMetrics

def test_classification_metrics():
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 0, 0, 1])
    
    metrics = EvaluationMetrics.calculate_classification_metrics(y_true, y_pred)
    
    assert 'accuracy' in metrics
    assert 'precision' in metrics
    assert 'recall' in metrics
    assert 'f1' in metrics
    assert isinstance(metrics['accuracy'], float)
