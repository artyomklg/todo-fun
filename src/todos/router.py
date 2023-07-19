from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException

from ..database import get_async_session, AsyncSession
from .schemas import Task, TaskCreate, TaskUpdate
from .models import TaskModel
from .dao import TaskDAO

router = APIRouter(prefix='/tasks', tags=['tasks'])


# Создание задачи
@router.post("")
async def create_task(task: TaskCreate, session: AsyncSession = Depends(get_async_session)) -> Task:
    task = await TaskDAO.add(session, task)
    await session.commit()
    return task


# Получение списка всех задач
@router.get("")
async def read_tasks(complit: Optional[bool] = None, session: AsyncSession = Depends(get_async_session)) -> List[Task]:
    filter_by = {}
    if complit is not None:
        filter_by.update({'complit': complit})
    tasks = await TaskDAO.find_all(session, **filter_by)
    return tasks


# Выполнение задачи
@router.post("/{task_id}")
async def complite_task(task_id: int, session: AsyncSession = Depends(get_async_session)) -> Task:
    task = await TaskDAO.find_one_or_none(session, id=task_id)
    if not task:
        raise HTTPException(404)

    complite_task = await TaskDAO.update(session, TaskModel.id == task_id, obj_in={'complite': True})
    await session.commit()
    return complite_task


# Получение задачи по ID
@router.get("/{task_id}")
async def read_task(task_id: int, session: AsyncSession = Depends(get_async_session)) -> Task:
    task = await TaskDAO.find_one_or_none(session, id=task_id)
    if not task:
        raise HTTPException(404)
    return Task


# Обновление задачи по ID
@router.put("/{task_id}")
async def update_task(task_id: int, task: TaskUpdate, session: AsyncSession = Depends(get_async_session)) -> Task:
    task_exist = await TaskDAO.find_one_or_none(session, id=task_id)
    if not task_exist:
        raise HTTPException(404)

    update_task = await TaskDAO.update(session, TaskModel.id == task_id, obj_in=task)
    await session.commit()
    return update_task


# Удаление задачи по ID
@router.delete("/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    task_exist = await TaskDAO.find_one_or_none(session, id=task_id)
    if not task_exist:
        raise HTTPException(404)

    await TaskDAO.delete(session, TaskModel.id == task_id)
    await session.commit()
    return {'msg': 'Task was deleted'}
