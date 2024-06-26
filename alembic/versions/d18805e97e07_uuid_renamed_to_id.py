"""uuid renamed to id

Revision ID: d18805e97e07
Revises: 7cbaa1a94270
Create Date: 2024-05-20 21:53:24.571724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd18805e97e07'
down_revision = '7cbaa1a94270'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.UUID(), nullable=False))
    op.create_unique_constraint(None, 'users', ['id'])
    op.drop_column('users', 'uuid')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'id')
    # ### end Alembic commands ###
