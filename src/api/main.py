from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from .routers import evaluation, health
import logging
from src.utils.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(evaluation.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    logger.info("Starting up application...")

@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting down application...")
