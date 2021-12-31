from enum import unique
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.expression import null

from core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(30), unique=True, nullable=False)
    docker_image = Column(String(4096), nullable=False)
    version = Column(String(30), nullable=False)
    gpu_device = Column(String(10), nullable=False)
    port_range = Column(String(20), nullable=False)