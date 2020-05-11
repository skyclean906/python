"""card_user_views relation

Revision ID: w0018
Revises: w0017
Create Date: 2017-03-02 12:15:56.894000

"""

# revision identifiers, used by Alembic.
revision = 'w0018'
down_revision = 'w0017'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card_user_views',
    sa.Column('card_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_column(u'card', 'views_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'card', sa.Column('views_count', sa.INTEGER(), server_default=sa.text(u'0'), autoincrement=False, nullable=False))
    op.drop_table('card_user_views')
    # ### end Alembic commands ###
