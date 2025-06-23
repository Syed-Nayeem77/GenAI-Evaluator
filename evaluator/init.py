# evaluator/__init__.py

"""
GenAI Evaluator Package

Provides:
- GenAIEvaluator class for computing NLP metrics
- BLEU and BERTScore computation functions
"""

from .evaluator import GenAIEvaluator
from .metrics import compute_bleu, compute_bertscore

__all__ = [
    "GenAIEvaluator",
    "compute_bleu",
    "compute_bertscore",
]

