from fastapi import APIRouter

from app.services.docker_service import get_containers

router = APIRouter(tags=["Docker"])


@router.get("/docker")
def docker_status():
    return get_containers()
