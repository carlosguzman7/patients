"""empty message

Revision ID: 614a07a67347
Revises: c6a3ba3f02e6
Create Date: 2023-01-28 10:55:19.463525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '614a07a67347'
down_revision = 'c6a3ba3f02e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.alter_column('od_rx',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('os_rx',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('pres_doc',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('glasses', schema=None) as batch_op:
        batch_op.alter_column('pres_doc',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=False)

    with op.batch_alter_table('glasses', schema=None) as batch_op:
        batch_op.alter_column('pres_doc',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.alter_column('pres_doc',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('os_rx',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('od_rx',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
