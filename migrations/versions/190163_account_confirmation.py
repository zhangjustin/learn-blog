"""account confirmation

Revision ID: 190163627111
Revises: 456a945560f6
Create Data: 2017-08-04

"""

revision = '190163627111'
down_revision = '456a945560f6'

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_clolumn('users', sa.Column('confirmed', sa.Boolean(), nullable=True))

def downgrade():
    op.drop_column('users', 'confirmed')
