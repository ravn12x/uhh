"""empty message

Revision ID: fc3a0366dd1c
Revises: ea2141667021
Create Date: 2022-12-13 15:08:34.633492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc3a0366dd1c'
down_revision = 'ea2141667021'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=140), nullable=True),
    sa.Column('yes', sa.Integer(), nullable=True),
    sa.Column('no', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz')
    # ### end Alembic commands ###
