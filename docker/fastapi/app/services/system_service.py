import platform
from datetime import datetime

import psutil


def bytes_to_gb(value: int) -> float:
    return round(value / (1024**3), 2)


def get_system_information():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time

    return {
        "hostname": platform.node(),
        "uptime": str(uptime).split(".")[0],
        "memory": {
            "total_gb": bytes_to_gb(memory.total),
            "used_gb": bytes_to_gb(memory.used),
            "available_gb": bytes_to_gb(memory.available),
            "percent": memory.percent,
        },
        "disk": {
            "total_gb": bytes_to_gb(disk.total),
            "used_gb": bytes_to_gb(disk.used),
            "free_gb": bytes_to_gb(disk.free),
            "percent": disk.percent,
        },
    }
