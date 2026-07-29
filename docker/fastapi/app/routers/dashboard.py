from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.docker_service import get_containers
from app.services.metrics_service import get_metrics

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    metrics = get_metrics()
    containers = get_containers()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "title": "Digital Operations Lab",
            "metrics": metrics,
	    "containers": containers,
        },
    )
