import datetime

from attrs import field
from sqlalchemy import UUID

from database.base import entity

@entity
class TodoModel:
    todo_id: UUID | None = None
    todo_text: str
    todo_date: datetime.date | None = None