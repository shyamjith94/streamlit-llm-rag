import streamlit as st
from streamlit_cookies_controller import CookieController
from dotenv import load_dotenv
from src.navigations import get_navigations
from src.st_state import AgentChatMessage
from src.st_state import UserData
from src.ui.pages.styles import navigation_css
from src.config.migration import make_migrations
load_dotenv()
def main():
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