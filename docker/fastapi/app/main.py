from fastapi import FastAPI
from app.config import settings

from app.routers.metrics import router as metrics_router
from app.routers.health import router as health_router
from app.routers.system import router as system_router
from app.routers.docker import router as docker_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend des Digital Operations Lab",
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Digital Operations Lab API",
        "status": "running",
    }


app.include_router(health_router)
app.include_router(system_router)
app.include_router(docker_router)
app.include_router(metrics_router)
