from evaluator.evaluator import GenAIEvaluator

def test_evaluator():
    references = ["The sky is blue"]
    predictions = ["The sky is blue"]
    evaluator = GenAIEvaluator(references, predictions)
    results = evaluator.evaluate()

    assert results["BLEU"] > 0.8
    assert results["BERTScore"]["f1"] > 0.8

if __name__ == "__main__":
    test_evaluator()
    print("All tests passed!")

