from fastapi import APIRouter
from app.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():
    return {
    "status": "healthy",
    "service": settings.APP_NAME,
    "version": settings.APP_VERSION,
    "environment": settings.APP_ENV,
    "hostname": settings.HOST_NAME,
}
