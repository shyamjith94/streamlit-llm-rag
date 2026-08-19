import streamlit as st
from src.ui.pages.styles import chat_css

def _welcome():
    st.html(
         """
        <div class="welcome">

            <div class="welcome-icon">
                🤖
            </div>

            <h1>
                How can I help you?
            </h1>

            <p>
                Ask questions about your connected knowledge base.
            </p>

        </div>
        """
    )

def _suggesions():
    st.html(
        """
        <div style="
            display:grid;
            grid-template-columns:repeat(2, 1fr);
            gap:10px;
            margin-bottom:20px;
        ">
            <div class="suggestion">
                📄 Summarize my documents
            </div>
            <div class="suggestion">
                🔍 Find information about...
            </div>
            <div class="suggestion">
                📊 Give me the key insights
            </div>
            <div class="suggestion">
                💡 Explain this in simple terms
            </div>
        </div>
        """
    )

def _footer():
    st.html(
        """
        <div class="chat-footer">
            AI-generated responses may contain inaccuracies.
            Verify important information with your source documents.
        </div>
        """
    )

def agent():
    chat_css()
    _welcome()
    _suggesions()

    prompt = st.chat_input(
        "Ask something about your knowledge base..."
    )

    _footer()
