# Auto generated 
"""makes changes to inventory model adds name and quantity

Revision ID: 03160cca2033
Revises: 7a208e731d11
Create Date: 2022-01-16 15:22:50.613812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03160cca2033'
down_revision = '7a208e731d11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory', sa.Column('name', sa.String(), nullable=True))
    op.add_column('inventory', sa.Column('total_quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventory', 'total_quantity')
    op.drop_column('inventory', 'name')
    # ### end Alembic commands ###
