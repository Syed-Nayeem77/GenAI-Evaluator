from fastapi import APIRouter, HTTPException
from src.api.schemas import EvaluationRequest, EvaluationResponse
from src.evaluation import Evaluator
from config.settings import settings
import logging

router = APIRouter(tags=["evaluation"])
logger = logging.getLogger(__name__)

# Initialize evaluator
try:
    evaluator = Evaluator(settings.MODEL_PATH)
except Exception as e:
    logger.error(f"Failed to initialize evaluator: {str(e)}")
    raise

@router.post("/evaluate", response_model=EvaluationResponse)
async def evaluate(request: EvaluationRequest):
    try:
        result = evaluator.evaluate(request.dict())
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        logger.error(f"Evaluation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
