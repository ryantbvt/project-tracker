''' Consolidates all routers into a single file '''

from fastapi import APIRouter
from app.api.v1.endpoints import tasks

api_router = APIRouter()

# load all endpoints of v1
api_router.include_router(tasks.router, prefix="/tasks")
