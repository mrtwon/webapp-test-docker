"""empty message

Revision ID: 90241a5880c7
Revises: 3059f055ca91
Create Date: 2024-11-21 11:15:53.719211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90241a5880c7'
down_revision: Union[str, None] = '3059f055ca91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("GRANT SELECT ON todo TO backend;")
    op.execute("GRANT INSERT ON todo TO backend;")


def downgrade() -> None:
    op.execute('REVOKE ALL ON todo FROM backend;')
