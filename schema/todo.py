import datetime
from uuid import UUID

from schema.base import BaseSchema


class TodoSchema(BaseSchema):
    todo_id: UUID
    todo_text: str
    todo_date: datetime.date


class CreateTodoSchema(BaseSchema):
    todo_text: str
