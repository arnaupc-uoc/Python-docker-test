"""migration

Revision ID: 7331bc5d3866
Revises: fafa32bf2db2
Create Date: 2023-08-04 18:42:31.510298

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7331bc5d3866'
down_revision = 'fafa32bf2db2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_emails', schema=None) as batch_op:
        batch_op.drop_index('email')

    op.drop_table('user_emails')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_emails',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('email_confirmed_at', mysql.DATETIME(), nullable=True),
    sa.Column('is_primary', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_emails_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('user_emails', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=False)

    # ### end Alembic commands ###
