from fastapi import APIRouter, HTTPException
import docker
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from core.schemas.container_schema import ContainerListResponse

router = APIRouter()
client = docker.from_env()

@router.get("/", response_model=ContainerListResponse)
def getContainerList():
    containerList = []
    try:
        containers = client.containers.list(all=True)
    except docker.errors.APIError:
        raise HTTPException(status_code=500, detail="Docker Error")
    for index in range(len(containers)):
        containerInfo = {
            "id": containers[index].short_id,
            "image": containers[index].image.tags[0],
            "name": containers[index].name,
            "status": containers[index].status,
        }
        containerList.append(containerInfo)
    return {
        "status": "SUCCESS",
        "result": containerList,
    }

@router.get("/{name}/stop")
def containerStop(
    name: str,
):
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
def containerDelete(
    name: str,
):
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
def containerRestart(
    name: str,
):
    try:
        client.containers.get(name).restart()
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="No Such Container")
    except docker.errors.APIError:
        raise HTTPException(status_code=404, detail="Docker Error")
    return {
        "status": "SUCCESS",
    }