"""criação da tabela users

Revision ID: 9c393afc8794
Revises: 
Create Date: 2025-05-15 23:29:04.570976
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
1
revision: str = '9c393afc8794'
down_revision: Union[str, None] = '1d8585e2194e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password', sa.String(length=256), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
    )

def downgrade():
    op.drop_table('users')
