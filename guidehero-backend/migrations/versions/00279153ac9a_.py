"""empty message

Revision ID: 00279153ac9a
Revises: a8b5adabbb0d
Create Date: 2016-10-27 01:04:31.153775

"""

# revision identifiers, used by Alembic.
revision = '00279153ac9a'
down_revision = 'a8b5adabbb0d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'card_likes_user_id_fkey', 'card_likes', type_='foreignkey')
    op.drop_constraint(u'card_likes_card_id_fkey', 'card_likes', type_='foreignkey')
    op.create_foreign_key(None, 'card_likes', 'card', ['card_id'], ['id'], ondelete='cascade')
    op.create_foreign_key(None, 'card_likes', 'user', ['user_id'], ['id'], ondelete='cascade')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'card_likes', type_='foreignkey')
    op.drop_constraint(None, 'card_likes', type_='foreignkey')
    op.create_foreign_key(u'card_likes_card_id_fkey', 'card_likes', 'card', ['card_id'], ['id'])
    op.create_foreign_key(u'card_likes_user_id_fkey', 'card_likes', 'user', ['user_id'], ['id'])
    ### end Alembic commands ###
