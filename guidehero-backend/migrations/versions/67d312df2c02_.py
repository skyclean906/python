"""empty message

Revision ID: 67d312df2c02
Revises: dd6f90adaf46
Create Date: 2016-10-18 01:43:39.806046

"""

# revision identifiers, used by Alembic.
revision = '67d312df2c02'
down_revision = 'dd6f90adaf46'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('published', sa.Boolean(), server_default='false', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'published')
    ### end Alembic commands ###
