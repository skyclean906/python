"""contribution field in user_role_card model

Revision ID: 5472e501f637
Revises: a07979b6882f
Create Date: 2016-11-25 09:49:51.138000

"""

# revision identifiers, used by Alembic.
revision = '5472e501f637'
down_revision = 'a07979b6882f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_role_card', sa.Column('contribution', sa.Integer(), server_default='0', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_role_card', 'contribution')
    ### end Alembic commands ###
