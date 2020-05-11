"""views user for card

Revision ID: w0016
Revises: w0015
Create Date: 2017-02-21 13:34:19.993000

"""

# revision identifiers, used by Alembic.
revision = 'w0016'
down_revision = 'w0015'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('views_count', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'views_count')
    # ### end Alembic commands ###