"""empty message

Revision ID: c6a3ba3f02e6
Revises: 771c51c1f628
Create Date: 2023-01-28 10:42:05.726125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6a3ba3f02e6'
down_revision = '771c51c1f628'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('od_rx', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('os_rx', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('pres_doc', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('patient_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'patients', ['patient_id'], ['id'])
        batch_op.drop_column('prescription')
        batch_op.drop_column('pres_od')

    with op.batch_alter_table('glasses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('od_rx', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('os_rx', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('pres_doc', sa.String(), nullable=True))
        batch_op.drop_column('prescription')
        batch_op.drop_column('pres_od')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=False)

    with op.batch_alter_table('glasses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pres_od', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('prescription', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_column('pres_doc')
        batch_op.drop_column('os_rx')
        batch_op.drop_column('od_rx')

    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pres_od', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('prescription', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('patient_id')
        batch_op.drop_column('pres_doc')
        batch_op.drop_column('os_rx')
        batch_op.drop_column('od_rx')

    # ### end Alembic commands ###
