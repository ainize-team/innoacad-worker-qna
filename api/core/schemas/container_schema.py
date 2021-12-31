from typing import List
from pydantic import BaseModel

class ContainerBase(BaseModel):
    id: str
    image: str
    name: str
    status: str

class ContainerListResponse(BaseModel):
    status: str
    result: List[ContainerBase] = []