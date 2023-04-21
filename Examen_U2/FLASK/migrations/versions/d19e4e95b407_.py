"""empty message

Revision ID: d19e4e95b407
Revises: 
Create Date: 2023-04-21 08:08:27.127680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd19e4e95b407'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('apellido', sa.String(length=255), nullable=True),
    sa.Column('promedio', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('disco_almacenamiento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('compañia', sa.String(length=255), nullable=True),
    sa.Column('tamaño', sa.String(length=255), nullable=True),
    sa.Column('tipo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('laptop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(length=255), nullable=True),
    sa.Column('procesador', sa.String(length=255), nullable=True),
    sa.Column('precio', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('platillo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('descripcion', sa.String(length=255), nullable=True),
    sa.Column('tamaño', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('refresco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('marca', sa.String(length=255), nullable=True),
    sa.Column('ml', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refresco')
    op.drop_table('platillo')
    op.drop_table('laptop')
    op.drop_table('disco_almacenamiento')
    op.drop_table('alumno')
    # ### end Alembic commands ###
