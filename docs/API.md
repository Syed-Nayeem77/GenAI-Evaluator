# GenAI-Evaluator API Documentation

## Base URL
`http://localhost:8000/api/v1`

## Endpoints

### Health Check
```
GET /health
```

Response:
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

### Evaluation
```
POST /evaluate
```

Request Body:
```json
{
  "text": "The input text to evaluate",
  "label": 1,
  "metadata": {}
}
```

Response:
```json
{
  "success": true,
  "result": {
    "prediction": 1,
    "metrics": {
      "accuracy": 0.95,
      "precision": 0.94,
      "recall": 0.96,
      "f1": 0.95
    }
  }
}
```
