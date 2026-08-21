import streamlit as st
from streamlit_cookies_controller import CookieController
from dotenv import load_dotenv
from src.navigations import get_navigations
from src.st_state import AgentChatMessage
from src.st_state import UserData
from src.ui.pages.styles import navigation_css
from src.config.migration import make_migrations
load_dotenv()




import os
import psycopg2
import streamlit as st

def test_db():
    database_url = "postgresql://neondb_owner:npg_6HPbFkwgr5dl@ep-quiet-hall-aymczit8-pooler.c-5.us-east-2.aws.neon.tech/streamlit_rag?sslmode=require&channel_binding=require"

    try:
        conn = psycopg2.connect(database_url)

        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()

        conn.close()

        st.success("PostgreSQL connection successful")
        st.write(result)

    except Exception as e:
        st.error(f"PostgreSQL connection failed: {type(e).__name__}")
        st.code(str(e))


def main():
    # test_db()
    make_migrations()
    navigation_css()

    if "agent" not in st.session_state:
        st.session_state.agent = AgentChatMessage()
    if "user_data" not in st.session_state:
        st.session_state.user_data = UserData()
    st.set_page_config(
        page_title="LLM RAG",
        page_icon="🤖",
        layout="wide",
    )
    page = st.navigation(get_navigations())
    page.run()

if __name__ == "__main__":
    main()