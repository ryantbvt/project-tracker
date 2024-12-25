''' Pydantic Model for Tasks '''

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from enum import Enum

from python_utils.logging.logging import init_logger

logger = init_logger()

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

# Class request to create a new task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int

    # TODO: add title validator. Cannot be empty

# When requesting to view a Task
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    project_id: int
    status: str
    created_at: datetime
    due_date: datetime
    creator_id: int
    assignee_id: Optional[int] = None
    collaborator_ids: List[int] = []

    # can add parent tasks in the future to create subtasks. Default parent_task = None, otherwise parent_task = task_id of parent task

# For requests to update a specific task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    creator_id: Optional[int] = None
    assignee_id: Optional[int] = None
    collaborator_ids: Optional[List[int]] = None