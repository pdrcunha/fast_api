"""criação da tabela livros alugados

Revision ID: 55b01c4b3d53
Revises: cd8585e2194e
Create Date: 2025-05-16 00:09:56.702839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55b01c4b3d53'
down_revision: Union[str, None] = '9c393afc8794'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'rent_books',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('book_id', sa.Integer, sa.ForeignKey('books.id'), nullable=False),
        sa.Column('rented_at', sa.DateTime, nullable=False),
        sa.Column('returned_at', sa.DateTime, nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('rent_books')
