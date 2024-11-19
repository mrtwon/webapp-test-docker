"""Initial migration

Revision ID: 3059f055ca91
Revises: f99591cae2ed
Create Date: 2024-11-18 10:44:57.221950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3059f055ca91'
down_revision: Union[str, None] = 'f99591cae2ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('INSERT INTO todo(todo_text) VALUES (\'one todo\')')
    op.execute('INSERT INTO todo(todo_text) VALUES (\'two todo\')')
    op.execute('INSERT INTO todo(todo_text) VALUES (\'three todo\')')
    op.execute('INSERT INTO todo(todo_text) VALUES (\'four todo\')')
    op.execute('INSERT INTO todo(todo_text) VALUES (\'five todo\')')


def downgrade() -> None:
    pass
