import streamlit as st
from streamlit_cookies_controller import CookieController
from src.models import Users
from typing import Optional


cookie_controller  = CookieController()

def show_or_hide_suggesion(value:bool):
    st.session_state.agent.suggestions = value

def suggesion_status():
    return st.session_state.agent.suggestions

def make_login_true(value:bool, user:Optional[Users] =None):
    st.session_state.user_data.logged_in = value
    if user is not None:
        init_user_data(user)
        remember_me(True, user)

def init_cookies():
    st.session_state.user_data.logged_in = False
    st.session_state.user_data.id = None
    st.session_state.user_data.name = ""
    st.session_state.user_data.email = ""

def restore_cookies():
    if st.session_state.user_data.logged_in:
        return True
    user_id = cookie_controller.get("user_id") 
    if user_id:
        st.session_state.user_data.id = int(user_id)
        st.session_state.user_data.logged_in = True
        return True
    return False    
        

def init_user_data(user_data:Users):
    st.session_state.user_data.id = user_data.id
    st.session_state.user_data.name = user_data.name
    st.session_state.user_data.email = user_data.email
    st.session_state.user_data.logged_in = True

def remember_me(remember:bool,user:Users):
    """
    Args:
        remember (bool): whether to remember the user
        user (User): user object
    """
    if remember:
        cookie_controller.set(
            "user_id",
            str(user.id),
            max_age=60 * 60 * 24 * 30,
        )
    else:
        cookie_controller.set(
            "user_id",
            str(user.id),
        )
    
    
    
def get_user_info():
    return st.session_state.user_data
def get_save_user_session_id():
    return st.session_state.user_data.session_id

def set_save_user_session_id(session_id:str):
    st.session_state.user_data.session_id = session_id

def logout_user():
    # st.switch_page(st.Page(login_page))
    st.session_state.clear()
    
  