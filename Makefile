.PHONY: install test lint format run docker-build docker-run clean

install:
	pip install -r requirements.txt -r requirements-dev.txt

test:
	pytest tests/ -v --cov=src --cov-report=html

lint:
	flake8 src/
	mypy src/
	black --check src/ tests/

format:
	black src/ tests/
	isort src/ tests/

run:
	uvicorn src.api.main:app --reload

docker-build:
	docker build -t genai-evaluator .

docker-run:
	docker run -p 8000:8000 genai-evaluator

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .coverage htmlcov .pytest_cache
