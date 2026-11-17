"""Health and service metadata endpoints."""

from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health", summary="Health check")
def health_check() -> dict[str, str]:
    """Return a lightweight process health response."""
    return {"status": "ok"}


@router.get("/", summary="Service information")
def service_info() -> dict[str, str]:
    """Return the service name and current environment."""
    settings = get_settings()
    return {
        "service": settings.app_name,
        "environment": settings.app_env,
        "status": "running",
    }
