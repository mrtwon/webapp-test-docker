from sqlalchemy import Table, Column, UUID, DATE, TEXT, func
from database.base import mapper_registry
from database.models import TodoModel

table_todo = Table(
    "todo",
    mapper_registry.metadata,
    Column('todo_id', UUID, server_default=func.uuid_generate_v1(),primary_key=True),
    Column('todo_text', TEXT, nullable=False),
    Column('todo_date', DATE, server_default=func.now().cast(DATE),nullable=False)
)

mapper_registry.map_imperatively(
    TodoModel,
    table_todo
)