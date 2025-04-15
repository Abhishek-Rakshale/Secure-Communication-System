"""Add timestamp to Message model

Revision ID: ce21e0811a60
Revises: 8b62506e9c23
Create Date: 2025-03-23 20:00:18.092767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce21e0811a60'
down_revision = '8b62506e9c23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['sender_id'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['receiver_id'], ['id'])
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###
