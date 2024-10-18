"""Initial migration

Revision ID: 1a19f58d123f
Revises: 
Create Date: 2024-10-19 02:18:19.753597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a19f58d123f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logo', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('internal_id', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('internal_id')
    )
    op.create_table('manufacturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('certificates', sa.Text(), nullable=True),
    sa.Column('internal_id', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('internal_id')
    )
    op.create_table('brands_manufacturers',
    sa.Column('brand_internal_id', sa.String(length=50), nullable=False),
    sa.Column('manufacturer_internal_id', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['brand_internal_id'], ['brand.internal_id'], ),
    sa.ForeignKeyConstraint(['manufacturer_internal_id'], ['manufacturer.internal_id'], ),
    sa.PrimaryKeyConstraint('brand_internal_id', 'manufacturer_internal_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('brands_manufacturers')
    op.drop_table('manufacturer')
    op.drop_table('brand')
    # ### end Alembic commands ###
