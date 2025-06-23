from evaluate import load

def compute_bleu(references, predictions):
    """
    Compute BLEU score using HuggingFace evaluate
    Format: predictions - list[str], references - list[list[str]]
    """
    metric = load("bleu")
    formatted_preds = [pred.strip() for pred in predictions]
    formatted_refs = [[ref.strip()] for ref in references]  # Each ref wrapped in list
    result = metric.compute(predictions=formatted_preds, references=formatted_refs)
    return result["bleu"]

def compute_bertscore(references, predictions):
    """
    Compute BERTScore using HuggingFace evaluate
    Format: both inputs are list[str]
    """
    metric = load("bertscore")
    result = metric.compute(predictions=predictions, references=references, lang="en")
    return {
        "precision": round(sum(result["precision"]) / len(result["precision"]), 4),
        "recall": round(sum(result["recall"]) / len(result["recall"]), 4),
        "f1": round(sum(result["f1"]) / len(result["f1"]), 4)
    }
