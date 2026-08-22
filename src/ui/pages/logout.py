import streamlit as st
from src.st_state import logout_user

from src.ui.pages.styles import login_css
def logout_page():
    login_css()
    st.markdown(
        """
        <div class="sidebar-logout-wrapper">
        """,
        unsafe_allow_html=True,
    )


    logout_user()
    st.rerun()

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True,
    )