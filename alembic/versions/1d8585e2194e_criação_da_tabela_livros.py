"""criação da tabela livros

Revision ID: 1d8585e2194e
Revises: 9c393afc8794
Create Date: 2025-05-16 00:09:24.127164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d8585e2194e'
down_revision: Union[str, None] = '0d8585e2194e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('author', sa.String(length=255), nullable=False),
        sa.Column('published_year', sa.Integer, nullable=True),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('books_categories.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('books')
