from abc import ABC
from uuid import UUID

from repository.repository_todo import TodoRepo, ITodoRepo
from schema import CreateTodoSchema, TodoSchema
from database import TodoModel

class TodoServiceABC(ABC):
    async def add_todo(self, schema: CreateTodoSchema) -> TodoSchema:
        ...

    async def get_todo(self, todo_id: UUID) -> TodoSchema:
        ...

    async def get_todo_list(self) -> list[TodoSchema]:
        ...


class TodoService(TodoServiceABC):
    def __init__(self):
        self.repo: ITodoRepo = TodoRepo()

    async def add_todo(self, schema: CreateTodoSchema) -> TodoSchema:
        new_todo = TodoModel(todo_text=schema.todo_text)
        r = await self.repo.add_todo(new_todo)
        return TodoSchema.model_validate(r)

    async def get_todo(self, todo_id: UUID) -> TodoSchema:
        repo_result = await self.repo.get_todo_by_id(todo_id)
        return TodoSchema.model_validate(repo_result)

    async def get_todo_list(self) -> list[TodoSchema]:
        repo_result = await self.repo.get_todo_list()
        return [TodoSchema.model_validate(one_row) for one_row in repo_result]
