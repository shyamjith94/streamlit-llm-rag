import streamlit as st
from src.ui.pages.home import home
from src.ui.pages.connector import connector
from src.ui.pages.agent import agent
from src.ui.pages.login import login_page
from src.ui.pages.register import register_page
from src.ui.pages.logout import logout_page

agent_page_obj =st.Page(
    agent,
    title="Agent",
    icon=":material/smart_toy:",
)


    
home_page_obj = st.Page(
    home,
    title="Home",
    icon=":material/home:",
    default=True,
    url_path="home"
)

connector_page_obj = st.Page(
    connector,
    title="Connector",
    icon=":material/extension:",
)

login_page_obj = st.Page(
    login_page,
    title="Login",
    icon=":material/extension:",
)

register_page_obj = st.Page(
    register_page,
    title="Register",
    icon=":material/extension:",    
    url_path="register_page"
)

logout_page_obj = st.Page(
    logout_page,
    title="Logout",
    icon=":material/logout:",
    url_path="logout_page"
)


def chat_button(page):

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.page_link(
            page,
            label="Start a conversation",
            icon=":material/chat:",
            use_container_width=True,
        )


authenticated_navigations = {
    "Home":[
        home_page_obj
    ],
    "Chat":[
        agent_page_obj,
        connector_page_obj
    ],
    "Logout":[
        logout_page_obj
    ]
}

unauthenticated_navigations = {
    "Account":[
        register_page_obj,
        login_page_obj
    ]
}



def get_navigations():  
    if st.session_state.user_data.logged_in:
        return authenticated_navigations
    else:
        return unauthenticated_navigations