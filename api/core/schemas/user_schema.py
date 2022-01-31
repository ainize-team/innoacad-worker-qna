from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str
    docker_image: str
    version: str
    gpu_device: str
    port_range: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "username": "innoacad16",
                "docker_image": "nvidia/cuda:11.1-base",
                "version": "1.0.0",
                "gpu_device": "2:1",
                "port_range": "11600-11610",
            },
        }
