"""Add patient table

Revision ID: 002
Revises: 001
Create Date: 2021-06-02 14:31:33.813799

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "patient",
        sa.Column(
            "id", sa.Integer, sa.Identity(always=True), nullable=False, primary_key=True
        ),
        sa.Column("email", sa.String(50), nullable=False, unique=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("date_of_birth", sa.Date, nullable=False),
    )


def downgrade():
    op.drop_table("patient")
