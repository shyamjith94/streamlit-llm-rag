import subprocess
import streamlit as st


# @st.cache_resource
def make_migrations():
    result = subprocess.run(["alembic", "upgrade", "head"])
    if result.returncode != 0:
        st.error("Migration failed")
        raise RuntimeError(f"Migration failed {result.stderr}")
    else:
        st.success("Migration completed")
    return True