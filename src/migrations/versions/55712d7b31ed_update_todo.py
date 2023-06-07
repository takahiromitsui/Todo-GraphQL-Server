"""Update Todo

Revision ID: 55712d7b31ed
Revises: 277b2137a85b
Create Date: 2023-06-07 14:04:59.005533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55712d7b31ed'
down_revision = '277b2137a85b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
