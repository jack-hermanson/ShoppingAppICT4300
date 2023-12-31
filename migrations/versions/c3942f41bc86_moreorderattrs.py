"""MoreOrderAttrs

Revision ID: c3942f41bc86
Revises: 62a874e0b549
Create Date: 2023-11-12 11:46:49.892045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3942f41bc86'
down_revision = '62a874e0b549'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('expiration', sa.String(length=5), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('street_address', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('city', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('state', sa.String(length=2), nullable=False))
        batch_op.add_column(sa.Column('zip_code', sa.String(length=5), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('zip_code')
        batch_op.drop_column('state')
        batch_op.drop_column('city')
        batch_op.drop_column('street_address')
        batch_op.drop_column('name')
        batch_op.drop_column('expiration')

    # ### end Alembic commands ###
