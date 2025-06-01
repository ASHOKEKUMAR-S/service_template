from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from .routes import router as routes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("service_apps")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting Service Apps API...")
    yield
    logger.info("🧹 Shutting down Service Apps API...")

app = FastAPI(
    title="Service Apps API",
    lifespan=lifespan
)

app.include_router(routes)
