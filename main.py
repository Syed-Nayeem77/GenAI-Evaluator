from evaluator.genai_evaluator import GenAIEvaluator

# Example usage
if __name__ == "__main__":
    references = ["The sky is blue", "It is raining"]
    predictions = ["The sky was blue", "It rains"]
    
    evaluator = GenAIEvaluator(references, predictions)
    scores = evaluator.evaluate()
    
    print("Evaluation Results:")
    for metric, value in scores.items():
        print(f"{metric}: {value}")
