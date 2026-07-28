from fastapi import APIRouter

from app.services.system_service import get_system_information

router = APIRouter(tags=["System"])


@router.get("/system")
def system():
    return get_system_information()
