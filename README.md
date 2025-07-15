# GenAI Evaluator

An extensible, production-grade framework to evaluate Generative AI outputs across tasks using custom and built-in metrics. It supports text, image, and multi-modal evaluation using both statistical metrics and LLM-as-a-judge paradigms.

---

##  Key Features

- **Multi-modal Evaluation** — Supports evaluation of text, image, and multi-modal generative outputs.
- **Modular Metric Design** — Includes 20+ reusable metrics like coherence, faithfulness, fluency, bias, toxicity.
- **LLM-as-a-Judge Integration** — Uses GPT-style LLMs to evaluate content with >80% alignment to human feedback.
- **Production Deployment** — Docker and Kubernetes compatible APIs.
- **Monitoring & Drift Detection** — Track model behavior over time and surface risks.
- **Developer Friendly** — Pydantic models, Jinja templates, easy-to-extend metric interfaces.

---

##  Project Structure

```

GenAI-Evaluator/
├── api/                 # FastAPI app for API exposure
├── clients/             # LLM client implementations (Azure, AWS, etc.)
├── flows/               # Workflow orchestration for evaluation
├── interfaces/          # Standardized input/output data schemas
├── metrics/             # Built-in metric implementations
├── templates/           # Jinja templates for prompt engineering
├── notebooks/           # Example usage in Jupyter
├── tests/               # Unit and integration tests
├── evaluation.ipynb     # Core example for using framework
├── requirements.txt     # Python dependencies
└── README.md

````

---

##  Installation

### Prerequisites
- Python 3.9+
- LLM API access (Azure OpenAI, AWS Bedrock, or Mistral)

### Setup


# Clone repository
git clone https://github.com/Syed-Nayeem77/GenAI-Evaluator.git
cd GenAI-Evaluator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
````

---

##  Quick Start

### 1. Evaluate with Built-in Metric

from clients.azure_openai import AzureClient
from metrics.faithfulness import FaithfulnessMetric

client = AzureClient(api_key="your-key")
metric = FaithfulnessMetric(client)
result = metric.evaluate(
    context="Paris is the capital of France",
    response="The French capital is Paris"
)

print(f"Faithfulness score: {result.score}")
```

### 2. Run the API Server


uvicorn api.main:app --reload
```

Then open: `http://localhost:8000/docs` to explore the Swagger UI.

---

##  Evaluation Metrics

| Category    | Metrics (Examples)            | Engine       |
| ----------- | ----------------------------- | ------------ |
| Quality     | Fluency, Coherence, Relevance | LLM-as-Judge |
| Safety      | Toxicity, Bias, Violence      | Classifier   |
| Factuality  | Faithfulness, Groundedness    | RAG/LLM      |
| Retrieval   | Precision, Recall, F1 Score   | Statistical  |
| Translation | COMET, BLEURT, METEOR         | Hybrid       |

 See full metric descriptions in `docs/METRICS.md`

---

##  Deployment

### Docker

```bash
docker build -t genai-evaluator .
docker run -p 8000:8000 genai-evaluator
```

### Kubernetes


kubectl apply -f k8s/deployment.yaml
```

---

##  Development Guidelines

### Add New Metric

1. Create new class under `metrics/`
2. Define schema in `interfaces/` if needed
3. Add Jinja template under `templates/`
4. Register in `flows/evaluation_flow.py`

### Run Tests


pytest tests/ --cov=src --cov-report=html
```


##  Ethical Guidelines

*  Avoid uploading sensitive or private data
*  Disclose AI assistance in any research evaluations
*  Monitor metrics to avoid amplifying bias or toxicity

---

##  Resources

*  API Docs → `http://localhost:8000/docs`
*  Example Notebooks → `notebooks/`
*  Deployment Guide → `docs/DEPLOYMENT.md`
*  Contribution Guide → `docs/CONTRIBUTING.md`

---
