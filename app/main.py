"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    settings = get_settings()
    application = FastAPI(
        title=settings.app_name,
        description=(
            "An engineering documentation assistant. "
            "RAG capabilities are introduced incrementally."
        ),
        version="0.1.0",
    )
    application.include_router(health_router)
    return application


app = create_app()
