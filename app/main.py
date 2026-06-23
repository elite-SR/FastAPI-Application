import logging
import time
from fastapi import FastAPI, HTTPException
from psycopg2 import connect
from redis import Redis
from app.config import settings

# Configure structured production logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("backend-api")

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {
        "status": "running",
        "message": "Welcome to the Production AI/Backend API",
        "timestamp": time.time()
    }

@app.get("/health")
def health_check():
    health_status = {
        "status": "healthy",
        "database": "unhealthy",
        "redis": "unhealthy",
        "timestamp": time.time()
    }
    errors = []

    # 1. Test PostgreSQL Connection
    try:
        conn = connect(settings.DATABASE_URL, connect_timeout=3)
        conn.close()
        health_status["database"] = "healthy"
        logger.info("Health check: Database connection OK")
    except Exception as e:
        errors.append(f"Database error: {str(e)}")
        logger.error(f"Health check failed: Database connection error: {e}")

    # 2. Test Redis Connection
    try:
        redis_client = Redis.from_url(settings.REDIS_URL, socket_timeout=3)
        if redis_client.ping():
            health_status["redis"] = "healthy"
            logger.info("Health check: Redis connection OK")
    except Exception as e:
        errors.append(f"Redis error: {str(e)}")
        logger.error(f"Health check failed: Redis connection error: {e}")

    # If any underlying dependency is down, mark overall status as unhealthy
    if health_status["database"] != "healthy" or health_status["redis"] != "healthy":
        health_status["status"] = "unhealthy"
        raise HTTPException(status_code=503, detail={"status": health_status, "errors": errors})

    return health_status
