"""Alter column data type

Revision ID: fc2c47cdc494
Revises: 6475768e8d9a
Create Date: 2023-09-24 15:50:43.643696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc2c47cdc494'
down_revision = '6475768e8d9a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('restaurant_pizza', sa.Column('temp_price', sa.Integer(), nullable=True))

    op.execute('UPDATE restaurant_pizza SET temp_price = CAST(price AS INTEGER)')

    # Remove the old column
    op.drop_column('restaurant_pizza', 'price')

    # Rename the new column to the original column name
    op.alter_column('restaurant_pizza', 'temp_price', new_column_name='price')


def downgrade():
    # Add a new column with the original data type
    op.add_column('restaurant_pizza', sa.Column('temp_price', sa.Float(), nullable=True))

    # Update the new column with the values from the old column (you may need to cast the values)
    op.execute('UPDATE restaurant_pizza SET temp_price = CAST(price AS FLOAT)')

    # Remove the old column
    op.drop_column('restaurant_pizza', 'price')

    # Rename the new column to the original column name
    op.alter_column('restaurant_pizza', 'temp_price', new_column_name='price')
