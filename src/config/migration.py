import subprocess
import streamlit as st
from pathlib import Path
from alembic.config import Config
from alembic import command

@st.cache_resource
def make_migrations():
    base_dir = Path(__file__).resolve().parents[2]

    alembic_cfg = Config(
        str(base_dir / "alembic.ini")
    )

    command.upgrade(alembic_cfg, "head")