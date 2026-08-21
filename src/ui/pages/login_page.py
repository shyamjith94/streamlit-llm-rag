from src.st_state.state_handle import init_user_data
import streamlit as st
from src.ui.pages.styles.login_css import login_css
from src.st_state import init_cookies, restore_cookies, remember_me
from src.services.auth import login_user
from src.utils import is_valid_email
from src.config.db import get_db
from src.ui.pages import home

def _login_form():

    with st.form("login_form"):

        email = st.text_input(
            "Email address",
            placeholder="you@example.com",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
        )

        remember = st.checkbox(
            "Remember me",
            value=True,
        )

        st.html(
            """
            <div class="forgot-password">
                <a href="#">Forgot password?</a>
            </div>
            """
        )

        submitted = st.form_submit_button(
            "Sign in  →",
            use_container_width=True,
            type="primary",
        )

        if submitted:

            if not email.strip() or not is_valid_email(email):
                st.error("Please enter a valid email address.")
                return

            if not password:
                st.error("Please enter your password.")
                return
            try:
               
                with get_db() as db:
                    user = login_user(email,password,db)
                    if user:
                        init_user_data(user)
                        remember_me(remember,user)
                        st.switch_page(st.Page(home))
                        st.success("Logged in successfully!")
                        
                    else:
                        st.error("You dont accoout registered!")
            except Exception as exc:
                print(exc)
                st.error("Please try after some time!")
            



def login_page():

    init_cookies()
    if restore_cookies():
        st.switch_page(st.Page(home))

    st.set_page_config(
        page_title="Sign In",
        page_icon="🔐",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    login_css()

    st.html(
        """
        <div class="login-logo">
            🔐
        </div>

        <div class="login-title">
            Welcome back
        </div>

        <div class="login-subtitle">
            Sign in to continue to your account
        </div>
        """
    )

    _login_form()

    st.html(
        """
        <div class="register-text">
            Don't have an account?
            <a class="register-link" href="/register_page">
                Create an account
            </a>
        </div>

        <div class="login-footer">
            Secure authentication · Your information is protected
        </div>
        """
    )