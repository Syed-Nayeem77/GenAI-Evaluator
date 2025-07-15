from pydantic import BaseModel
from typing import Optional

class EvaluationRequest(BaseModel):
    text: str
    label: Optional[int] = None
    metadata: Optional[dict] = None

class EvaluationResponse(BaseModel):
    success: bool
    result: dict
