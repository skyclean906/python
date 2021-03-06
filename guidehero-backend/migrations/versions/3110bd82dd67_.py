"""empty message

Revision ID: 3110bd82dd67
Revises: edad351a6f72
Create Date: 2016-10-25 23:35:13.778397

"""

# revision identifiers, used by Alembic.
revision = '3110bd82dd67'
down_revision = 'edad351a6f72'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card_likes',
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('card_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'card_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card_likes')
    ### end Alembic commands ###
