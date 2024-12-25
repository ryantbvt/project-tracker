from fastapi import APIRouter

from app.schemas.tasks import TaskCreate, TaskResponse

router = APIRouter()

@router.post("/", response_model=TaskResponse)
async def create_task():
    return {"message": "Hello World"}

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task():
    pass