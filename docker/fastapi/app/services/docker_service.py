import docker

client = docker.from_env()


def get_containers():
    containers = []

    for container in client.containers.list(all=True):

        health = None

        if "Health" in container.attrs["State"]:
            health = container.attrs["State"]["Health"]["Status"]

        containers.append(
            {
                "name": container.name,
                "image": container.image.tags[0]
                if container.image.tags
                else "unknown",
                "status": container.status,
                "health": health,
            }
        )

    return containers
