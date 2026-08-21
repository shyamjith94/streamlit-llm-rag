import subprocess
import streamlit as st


# @st.cache_resource
def make_migrations():
    result = subprocess.run(
        ["alembic", "upgrade", "head"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("Migration failed")