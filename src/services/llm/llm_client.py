from langchain_groq import ChatGroq
import streamlit as st
from src.config import settings

def _valid_groq_api_key() -> bool:
    """Check if the Groq API key is valid"""
    if settings.groq_api_key == "":
        return False
    return True

    
@st.cache_resource
def get_llm_client():
    if _valid_groq_api_key():
        return ChatGroq(
            # model="openai/gpt-oss-20b",
            model="openai/gpt-oss-120b",
            # max_tokens=20000,
            temperature=0.2,
            api_key=settings.groq_api_key,
            streaming=True
        )
    else:
        raise ValueError("❌ Missing Groq API Key. Please set the GROQ_API_KEY environment variable.")