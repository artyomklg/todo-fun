from ..dao import BaseDAO
from .models import TaskModel
from .schemas import Task, TaskCreate, TaskUpdate


class TaskDAO(BaseDAO[TaskModel, TaskCreate, TaskUpdate]):
    model = TaskModel
