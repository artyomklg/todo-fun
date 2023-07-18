from typing import Optional
from pydantic import BaseModel, ConfigDict

class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class TaskCreate(TaskBase):
    title: str


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    title: str
    description: str
    complite: bool

    model_config = ConfigDict(from_attributes=True)
