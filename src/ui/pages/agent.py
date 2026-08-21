import streamlit as st
from src.ui.pages.styles import agent_css
from src.st_state import show_or_hide_suggesion,suggesion_status
from src.services.llm.graph import invoke_graph


def _header():
    st.html(
          """
        <div class="chat-header">

            <div class="chat-header-left">

                <div class="chat-logo">
                    🤖
                </div>

                <div>
                    <div class="chat-title">
                        RAG Assistant
                    </div>

                    <div class="chat-subtitle">
                        Knowledge Base Assistant
                    </div>
                </div>

            </div>

            <div class="online-status">
                <div class="online-dot"></div>
                Ready
            </div>

        </div>
        """
    )

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
    with st.chat_message("assistant"):
        st.html("Hello! How can I help you?")



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
    agent_css()
    _header()
    _welcome()

    prompt = st.chat_input(
        "Ask something about your knowledge base..."
    )
    if prompt:
        show_or_hide_suggesion(False)
        with st.chat_message("user"):
            st.html(prompt)
        # with st.chat_message("assistant"):
        #     st.write_stream(get_response(prompt))
        with st.spinner("Thinking..."):
            st.write_stream(invoke_graph(prompt))
    if suggesion_status():
        _suggesions()


   
    
    
    
    _footer()
