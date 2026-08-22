import streamlit as st
from src.ui.pages.styles.register_css import register_css
from src.services.auth import register_user
from src.models import Users
from src.config.db import get_db
from src.ui.pages import home
from src.st_state.state_handle import make_login_true
from src.utils import is_valid_email





def _verify_register_form(name:str,email:str,password:str,confirm_password:str):
    if not name.strip():
        st.error("Please enter your full name.")
        return False

    if not email.strip() or not is_valid_email(email):
        st.error("Please enter a valid email address.")
        return False

    if not password:
        st.error("Please enter a password.")
        return False

    if len(password) < 8:
        st.error("Password must contain at least 8 characters.")
        return False

    if password != confirm_password:
        st.error("Passwords do not match.")
        return False
    return True

def _register_form():

    with st.form("register_form"):

        name = st.text_input(
            "Full name",
            placeholder="John Doe",
        )

        email = st.text_input(
            "Email address",
            placeholder="you@example.com",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a strong password",
        )

        st.html(
            """
            <div class="password-hint">
                Use at least 8 characters with a mix of letters and numbers.
            </div>
            """
        )

        confirm_password = st.text_input(
            "Confirm password",
            type="password",
            placeholder="Re-enter your password",
        )

        st.html("<div style='height: 8px'></div>")

        submitted = st.form_submit_button(
            "Create account  →",
            use_container_width=True,
            type="primary",
        )

        if submitted:
            try:
                if _verify_register_form(name,email,password,confirm_password):
                    with get_db() as db:
                        user = register_user(Users(name=name,email=email,password=password), db)
                    st.success("Account created successfully!")
                    make_login_true(True, user)
                    st.switch_page(st.Page(home))
                else:
                    st.success("Please provide proper input!")
            except Exception as exc:
                print(exc)
                st.error("Please try after some time!")
            
            

                

            


def register_page():
    

    st.set_page_config(
        page_title="Create Account",
        page_icon="✨",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    register_css()

   

    st.html(
        """
        <div class="register-card">

            <div class="register-logo">
                ✨
            </div>

            <div class="register-title">
                Create your account
            </div>

            <div class="register-subtitle">
                Join us and get started in just a few seconds.
            </div>
        """
    )

    _register_form()

    st.html(
        """
            <div class="login-text">
                Already have an account?
                <a class="login-link" href="/login_page">
                    Sign in
                </a>
            </div>

            <div class="register-footer">
                By creating an account, you agree to our
                Terms of Service and Privacy Policy.
            </div>

        </div>
        """
    )