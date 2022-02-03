"""Add Jenis Pelayanan

Revision ID: 94cd14034298
Revises: e4f676c1b384
Create Date: 2022-02-03 10:15:09.196017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94cd14034298'
down_revision = 'e4f676c1b384'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sep_request', sa.Column('jnsPelayanan', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sep_request', 'jnsPelayanan')
    # ### end Alembic commands ###