from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])

class HealthStatus(BaseModel):
    status: str
    version: str

@router.get("/health", response_model=HealthStatus)
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }
