"""Re-sincronizar estado das migrações

Revision ID: 4a74d7a63ec9
Revises: 
Create Date: 2024-05-29 15:21:59.008303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a74d7a63ec9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.drop_constraint('games_creator_key', type_='unique')
        batch_op.drop_constraint('games_gameName_key', type_='unique')
        batch_op.drop_constraint('games_secondGameName_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.create_unique_constraint('games_secondGameName_key', ['secondGameName'])
        batch_op.create_unique_constraint('games_gameName_key', ['gameName'])
        batch_op.create_unique_constraint('games_creator_key', ['creator'])
        batch_op.alter_column('price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)

    # ### end Alembic commands ###
