from app.services.docker_service import get_containers
from app.services.system_service import get_system_information


def get_metrics():

    containers = get_containers()
    system = get_system_information()

    running = len(
        [
            container
            for container in containers
            if container["status"] == "running"
        ]
    )

    stopped = len(
        [
            container
            for container in containers
            if container["status"] != "running"
        ]
    )

    return {
        "containers": {
            "total": len(containers),
            "running": running,
            "stopped": stopped,
        },
        "system": {
            "memory_percent": system["memory"]["percent"],
            "disk_percent": system["disk"]["percent"],
        },
    }
