"""Add created_at column to books

Revision ID: f095017c9e6e
Revises: cc7cc1ba89cc
Create Date: 2025-02-17 16:50:02.453320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f095017c9e6e'
down_revision: Union[str, None] = 'cc7cc1ba89cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.add_column('books', sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False))

def downgrade():
    op.drop_column('books', 'created_at')


