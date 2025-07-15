from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from src.api.routers import evaluation, health
from src.utils.logging import configure_logging

configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="API for evaluating GenAI model outputs"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(evaluation.router)
app.include_router(health.router)

@app.on_event("startup")
async def startup_event():
    # Initialize model and other resources
    pass
