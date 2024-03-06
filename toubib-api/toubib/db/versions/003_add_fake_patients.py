"""Add fake patients

Revision ID: 003
Revises: 002

"""
import sqlalchemy as sa
from alembic import op
from faker import Faker

revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade():
    metadata = sa.MetaData()
    metadata.reflect(bind=op.get_bind())

    patient_table = metadata.tables["patient"]
    doctor_table = metadata.tables["doctor"]

    faker = Faker()

    op.bulk_insert(
        patient_table,
        [
            {
                "email": faker.unique.email(),
                "first_name": faker.first_name(),
                "last_name": faker.last_name(),
                "date_of_birth": faker.date_of_birth(),
            }
            for _ in range(135)
        ],
    )

    op.bulk_insert(
        doctor_table,
        [
            {
                "first_name": faker.first_name(),
                "last_name": faker.last_name(),
                "hiring_date": faker.past_date(),
                "specialization": faker.bs(),
            }
            for _ in range(27)
        ],
    )


def downgrade():
    pass
