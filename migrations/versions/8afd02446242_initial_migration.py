"""Initial migration.

Revision ID: 8afd02446242
Revises: 
Create Date: 2024-03-17 12:43:04.076022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8afd02446242'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_equipo_nombre'), ['nombre'], unique=True)

    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('universidad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('participante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=128), nullable=False),
    sa.Column('correo_institucional', sa.String(length=128), nullable=False),
    sa.Column('edad', sa.Integer(), nullable=False),
    sa.Column('universidad_id', sa.Integer(), nullable=False),
    sa.Column('carrera', sa.String(length=128), nullable=False),
    sa.Column('sexo', sa.String(length=64), nullable=False),
    sa.Column('participacion_hackathon', sa.Boolean(), nullable=False),
    sa.Column('tipo_inscripcion', sa.String(length=64), nullable=False),
    sa.Column('rol_id', sa.Integer(), nullable=False),
    sa.Column('id_equipo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_equipo'], ['equipo.id'], ),
    sa.ForeignKeyConstraint(['rol_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['universidad_id'], ['universidad.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo_institucional')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participante')
    op.drop_table('universidad')
    op.drop_table('role')
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_equipo_nombre'))

    op.drop_table('equipo')
    # ### end Alembic commands ###
