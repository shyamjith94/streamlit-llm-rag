import streamlit as st
from dotenv import load_dotenv
from src.ui.navigation import navigations

load_dotenv()

st.set_page_config(
    page_title="LLM RAG",
    page_icon="🤖",
    layout="wide",
)
page = st.navigation(navigations)
page.run()