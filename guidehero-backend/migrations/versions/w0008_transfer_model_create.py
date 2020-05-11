"""Transfer model create

Revision ID: w0008
Revises: w0007
Create Date: 2016-12-19 14:34:36.890000

"""

# revision identifiers, used by Alembic.
revision = 'w0008'
down_revision = 'w0007'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'transfer',
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('user_from_id', sa.String(length=255), nullable=True),
        sa.Column('user_to_id', sa.String(length=255), nullable=True),
        sa.Column('amount', sa.Integer(), server_default='0', nullable=False),
        sa.Column('transaction_type', sa.String(), server_default='', nullable=False),
        sa.ForeignKeyConstraint(['user_from_id'], ['user.id'], ),
        sa.ForeignKeyConstraint(['user_to_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transfer')
    ### end Alembic commands ###
