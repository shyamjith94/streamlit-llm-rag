import streamlit as st
from src.ui.pages.home import home
from src.ui.pages.connector import connector
from src.ui.pages.agent import agent

agent_page =st.Page(
    agent,
    title="Agent",
    icon=":material/smart_toy:",
)

def home_page():
    return home(agent_page)

    
home_page = st.Page(
    home_page,
    title="Home",
    icon=":material/home:",
    default=True,
)

connector_page = st.Page(
    connector,
    title="Connector",
    icon=":material/extension:",
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


navigations = {
    "Home":[
        home_page
    ],
    "Chat":[
        agent_page,
        connector_page
    ]
}