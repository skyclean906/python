"""is_answer_on_card

Revision ID: w0004
Revises: w0003
Create Date: 2016-12-06 15:47:37.567000

"""

# revision identifiers, used by Alembic.
revision = 'w0004'
down_revision = 'w0003'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('is_answer', sa.Boolean(), server_default='false', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'is_answer')
    ### end Alembic commands ###
