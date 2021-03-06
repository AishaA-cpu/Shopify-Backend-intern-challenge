# Auto generated 
"""makes changes to shipment and inventory models, adds new attributes

Revision ID: 0425b9e03969
Revises: 1a60cd91ff95
Create Date: 2022-01-19 20:07:00.347936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0425b9e03969'
down_revision = '1a60cd91ff95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('inventory', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('inventory', 'price',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('inventory', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('shipment', sa.Column('breadth', sa.Float(), nullable=False))
    op.alter_column('shipment', 'length',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('shipment', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('shipment', 'weight',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('shipment', 'width',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.drop_column('shipment', 'breath')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shipment', sa.Column('breath', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.alter_column('shipment', 'width',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('shipment', 'weight',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('shipment', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('shipment', 'length',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.drop_column('shipment', 'breadth')
    op.alter_column('inventory', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('inventory', 'price',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('inventory', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
