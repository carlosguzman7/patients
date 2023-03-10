"""empty message

Revision ID: 42f62840e251
Revises: 
Create Date: 2023-01-04 20:47:39.929957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42f62840e251'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('date_of_birth', sa.DateTime(timezone=False), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('current_clrx', sa.Integer(), nullable=True),
    sa.Column('current_srx', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    # ### end Alembic commands ###
