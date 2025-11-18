"""add content column to posts table

Revision ID: a24cb729ca26
Revises: fe31b2adc067
Create Date: 2025-11-17 22:38:34.864399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a24cb729ca26'
down_revision: Union[str, Sequence[str], None] = 'fe31b2adc067'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
