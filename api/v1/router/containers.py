from fastapi import APIRouter, HTTPException
import docker
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from core.schemas.container_schema import ContainerListResponse

router = APIRouter()
client = docker.DockerClient(base_url='unix://var/run/docker.sock')


@router.get("/", response_model=ContainerListResponse)
def getContainerList():
    """
    Get all container's information list in host:

    - **id**: container id
    - **image**: conatiner image name
    - **name**: container name
    - **status**: container status
    """
    containerList = []
    try:
        containers = client.containers.list(all=True)
    except docker.errors.APIError:
        raise HTTPException(status_code=500, detail="Docker Error")
    for container in containers:
        containerInfo = {
            "id": container.short_id,
            "image": container.image.tags[0],
            "name": container.name,
            "status": container.status,
        }
        containerList.append(containerInfo)
    return {
        "status": "SUCCESS",
        "result": containerList,
    }


@router.get("/{name}/stop")
def containerStop(name: str,):
    """
    Request to terminate the container.
    \f
    :param name: Container Name
    """
    try:
        client.containers.get(name).stop()
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="No Such Container")
    except docker.errors.APIError:
        raise HTTPException(status_code=404, detail="Docker Error")
    return {
        "status": "SUCCESS",
    }


@router.get("/{name}/remove")
def containerDelete(name: str,):
    """
    Request to remove the container.
    \f
    :param name: Container Name
    """
    try:
        client.containers.get(name).remove()
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="No Such Container")
    except docker.errors.APIError:
        raise HTTPException(status_code=404, detail="Docker Error")
    return {
        "status": "SUCCESS",
    }


@router.get("/{name}/restart")
def containerRestart(name: str,):
    """
    Request to restart the container.
    \f
    :param name: Container Name
    """
    try:
        client.containers.get(name).restart()
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="No Such Container")
    except docker.errors.APIError:
        raise HTTPException(status_code=404, detail="Docker Error")
    return {
        "status": "SUCCESS",
    }
