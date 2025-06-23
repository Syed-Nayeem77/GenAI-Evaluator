from evaluator.metrics import compute_bleu, compute_bertscore

class GenAIEvaluator:
    def __init__(self, references, predictions):
        # Convert token lists to full sentences if needed
        self.references = [" ".join(ref) if isinstance(ref, list) else ref for ref in references]
        self.predictions = [" ".join(pred) if isinstance(pred, list) else pred for pred in predictions]

    def evaluate(self):
        bleu = compute_bleu(self.references, self.predictions)
        bertscore = compute_bertscore(self.references, self.predictions)
        return {
            "BLEU": round(bleu, 4),
            "BERTScore": bertscore
        }
