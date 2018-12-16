"""debt  table

Revision ID: c60865641a2e
Revises: b88582e5d669
Create Date: 2018-12-03 16:36:11.796260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c60865641a2e'
down_revision = 'b88582e5d669'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('debt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payer', sa.Integer(), nullable=False),
    sa.Column('receiver', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['payer'], ['user.id'], ),
    sa.ForeignKeyConstraint(['receiver'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_table('debt')
    # ### end Alembic commands ###