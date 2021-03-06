"""prize and total_likes fields to user_role_card table

Revision ID: w0001
Revises: 9c86084b2cad
Create Date: 2016-12-01 08:51:18.071000

"""

# revision identifiers, used by Alembic.
revision = 'w0001'
down_revision = '9c86084b2cad'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_role_card', sa.Column('prize', sa.Integer(), server_default='0', nullable=False))
    op.add_column('user_role_card', sa.Column('total_likes', sa.Integer(), server_default='0', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_role_card', 'total_likes')
    op.drop_column('user_role_card', 'prize')
    ### end Alembic commands ###
