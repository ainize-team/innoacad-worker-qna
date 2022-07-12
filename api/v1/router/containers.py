from fastapi import APIRouter, Depends, HTTPException
import docker
from sqlalchemy.orm import Session

from core.database import get_db

from core.models.user_model import UserModel

from core.schemas.container_schema import ContainerListResponse, ContainerPatchRequest

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
        raise HTTPException(status_code=500, detail="Docker Error")
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
        raise HTTPException(status_code=500, detail="Docker Error")
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
        raise HTTPException(status_code=500, detail="Docker Error")
    return {
        "status": "SUCCESS",
    }

@router.patch("/{name}/image")
def containerPatch(name: str, containerPatchRequest: ContainerPatchRequest, db: Session = Depends(get_db)):
    """
    Request to patch the container

    - **docker_image**: Container Image Name
    \f
    :param name: Container Name
    """
    try:
        container = client.containers.get(name)
        user = db.query(UserModel).filter(UserModel.username == name).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User Not Found")
        if container.status == "running":
            container.stop()
        client.images.pull(containerPatchRequest.repository, tag=containerPatchRequest.tag)
        user.docker_image = containerPatchRequest.repository + ':' + containerPatchRequest.tag
        db.commit()
        db.refresh(user)
        container.remove()
        return {
            "status": "SUCCESS",
        }
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="No Such Container or Image")
    except docker.errors.APIError:
        raise HTTPException(status_code=500, detail="Docker Error")
    except:
        raise HTTPException(status_code=500, detail="Server Error")