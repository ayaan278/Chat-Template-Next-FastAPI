from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.staticfiles import StaticFiles
from app.utils.logging import logger
from app.core.config import settings

# Create the FastAPI app
app = FastAPI(
    title="FastAPI Backend",
    description="API for backend services.",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=[
        "Accept",
        "Accept-Language",
        "Content-Language",
        "Content-Type",
        "Authorization",
        "X-Requested-With",
        "Origin",
        "Cache-Control",
        "Pragma",
        "X-Real-IP",
        "X-Forwarded-For",
        "X-Forwarded-Proto",
    ],
    expose_headers=["*"],
    max_age=3600,  # Cache preflight requests for 1 hour
)

# Include routers from different modules
from app.api.chats.routes import router as chats_router
# Static files for frontend
app.include_router(chats_router)

@app.on_event("startup")
def startup():
    logger.info("🚀 API started successfully")
    logger.info(f"📊 Environment: Development")

@app.get("/health", tags=["health"])
def health():
    """
    Simple health endpoint to check if the backend is running.
    """
    return {
        "status": "ok",
        "service": "API",
        "version": "1.1.0",
        "environment": "development",
        "ssl": True,
        "timestamp": "2025-06-21"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  # Bind to localhost only (Nginx will proxy)
        port=8000,
        reload=True,
        proxy_headers=True,  # Trust proxy headers
        forwarded_allow_ips="127.0.0.1"  # Allow forwarded IPs from localhost
    )
