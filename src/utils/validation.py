from typing import Any, Dict
from pydantic import BaseModel, ValidationError

def validate_input(data: Dict[str, Any], model: BaseModel) -> Dict[str, Any]:
    """Validate input data against Pydantic model"""
    try:
        return model(**data).dict()
    except ValidationError as e:
        raise ValueError(f"Validation error: {str(e)}")
