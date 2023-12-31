"""empty message

Revision ID: 2230e48342d7
Revises: aefdd473700e
Create Date: 2023-10-18 22:50:53.254567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2230e48342d7'
down_revision = 'aefdd473700e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key("cart_account_id", 'account', ['account_id'], ['account_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.drop_constraint("cart_account_id", type_='foreignkey')
        batch_op.drop_column('account_id')

    # ### end Alembic commands ###
