"""empty message

Revision ID: 4612b12143a2
Revises: d595a12705af
Create Date: 2023-04-01 00:04:38.081450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4612b12143a2'
down_revision = 'd595a12705af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=512), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_created_at'), 'notification', ['created_at'], unique=False)
    op.create_index(op.f('ix_notification_id'), 'notification', ['id'], unique=False)
    op.create_index(op.f('ix_notification_user_id'), 'notification', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_notification_user_id'), table_name='notification')
    op.drop_index(op.f('ix_notification_id'), table_name='notification')
    op.drop_index(op.f('ix_notification_created_at'), table_name='notification')
    op.drop_table('notification')
    # ### end Alembic commands ###
