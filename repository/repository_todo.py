from abc import ABC
from uuid import UUID

from sqlalchemy import select

from database import TodoModel
from database.base import SqlAlchemyRepo


class ITodoRepo(SqlAlchemyRepo, ABC):
    async def add_todo(self, todo: TodoModel) -> TodoModel:
        ...

    async def get_todo_by_id(self, todo_id: UUID) -> TodoModel:
        ...

    async def get_todo_list(self) -> list[TodoModel]:
        ...


class TodoRepo(ITodoRepo):

    async def add_todo(self, todo: TodoModel) -> TodoModel:
        session = await self.get_session()
        session.add(todo)
        await session.commit()
        return todo

    async def get_todo_by_id(self, todo_id: UUID) -> TodoModel:
        session = await self.get_session()
        stmt = select(TodoModel).where(TodoModel.todo_id == todo_id)
        r = await session.scalar(stmt)
        return r

    async def get_todo_list(self) -> list[TodoModel]:
        session = await self.get_session()
        stmt = select(TodoModel)
        r = await session.scalars(stmt)
        return r.all()
