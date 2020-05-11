"""points on user model

Revision ID: adff30e87615
Revises: 46b8f304418c
Create Date: 2016-11-29 11:01:45.177000

"""

# revision identifiers, used by Alembic.
revision = 'adff30e87615'
down_revision = '46b8f304418c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('points', sa.Integer(), server_default='0', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'points')
    ### end Alembic commands ###
