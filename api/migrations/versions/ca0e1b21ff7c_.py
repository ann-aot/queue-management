"""empty message

Revision ID: ca0e1b21ff7c
Revises: 6c1511e233c6
Create Date: 2018-10-09 15:58:45.052995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca0e1b21ff7c'
down_revision = '6c1511e233c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'csr', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'csr', type_='unique')
    # ### end Alembic commands ###
