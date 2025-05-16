"""criação da tabela categorias livros

Revision ID: 0d8585e2194e
Revises: 55b01c4b3d53
Create Date: 2025-05-16 00:19:22.439275

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d8585e2194e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books_categories',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('categorie', sa.String(length=255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('books_categories')
