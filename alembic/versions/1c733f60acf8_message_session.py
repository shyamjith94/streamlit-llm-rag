"""message , session

Revision ID: 1c733f60acf8
Revises: 34d2d72ebf0b
Create Date: 2026-08-22 20:45:03.431477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c733f60acf8'
down_revision: Union[str, Sequence[str], None] = '34d2d72ebf0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():

    # -------------------------------------------------
    # 1. Add UUID column to chat_sessions
    # -------------------------------------------------

    op.add_column(
        "chat_sessions",
        sa.Column(
            "session_id",
            postgresql.UUID(as_uuid=True),
            nullable=True,
        ),
    )

    # Generate UUID for existing sessions
    op.execute("""
        UPDATE chat_sessions
        SET session_id = gen_random_uuid()
        WHERE session_id IS NULL
    """)

    # Make session_id NOT NULL
    op.alter_column(
        "chat_sessions",
        "session_id",
        nullable=False,
    )

    # Unique index
    op.create_index(
        "ix_chat_sessions_session_id",
        "chat_sessions",
        ["session_id"],
        unique=True,
    )


    # -------------------------------------------------
    # 2. Remove old FK
    # -------------------------------------------------

    op.drop_constraint(
        "chat_messages_session_id_fkey",
        "chat_messages",
        type_="foreignkey",
    )


    # -------------------------------------------------
    # 3. Add temporary UUID column
    # -------------------------------------------------

    op.add_column(
        "chat_messages",
        sa.Column(
            "new_session_id",
            postgresql.UUID(as_uuid=True),
            nullable=True,
        ),
    )


    # -------------------------------------------------
    # 4. Convert old integer FK → UUID
    # -------------------------------------------------

    op.execute("""
        UPDATE chat_messages cm
        SET new_session_id = cs.session_id
        FROM chat_sessions cs
        WHERE cm.session_id = cs.id
    """)


    # -------------------------------------------------
    # 5. Remove old integer column
    # -------------------------------------------------

    op.drop_column(
        "chat_messages",
        "session_id",
    )


    # -------------------------------------------------
    # 6. Rename UUID column
    # -------------------------------------------------

    op.alter_column(
        "chat_messages",
        "new_session_id",
        new_column_name="session_id",
    )


    # -------------------------------------------------
    # 7. Make UUID column NOT NULL
    # -------------------------------------------------

    op.alter_column(
        "chat_messages",
        "session_id",
        nullable=False,
    )


    # -------------------------------------------------
    # 8. Create index
    # -------------------------------------------------

    op.create_index(
        "ix_chat_messages_session_id",
        "chat_messages",
        ["session_id"],
    )


    # -------------------------------------------------
    # 9. Create new UUID → UUID FK
    # -------------------------------------------------

    op.create_foreign_key(
        "chat_messages_session_id_fkey",
        "chat_messages",
        "chat_sessions",
        ["session_id"],
        ["session_id"],
    )