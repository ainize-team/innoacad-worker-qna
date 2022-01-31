from fastapi import FastAPI

from v1.router import users, containers

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(containers.router, prefix="/containers", tags=["containers"])
