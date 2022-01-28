from typing import List, Optional
from pydantic import BaseModel


class ContainerBase(BaseModel):
    id: str
    image: str
    name: str
    status: str

class ContainerPatchRequest(BaseModel):
    repository: str
    tag: str

class ContainerListResponse(BaseModel):
    status: str
    result: List[ContainerBase] = []
