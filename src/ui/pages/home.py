from src.ui.pages import agent
import streamlit as st
from src.ui.pages.styles import home_css

def _baner_data():
    st.html(
        """
        <div class="hero">
            <div class="hero-icon">🤖</div>

            <h1>LLM RAG Assistant</h1>
            <p>
                Ask questions, search your knowledge base,
                and get AI-powered answers grounded in your documents.
            </p>
        </div>
        """,
    )

def _feature_data():
    st.html(
    """
    <div class="section-title">
        <h2>Everything you need to work with your knowledge</h2>
        <p>
            A simple workflow from documents to intelligent answers.
        </p>
    </div>
    """
    )
    features = [
        (
            "📚",
            "Knowledge Base",
            "Organize your documents into a searchable knowledge base."
        ),
        (
            "🔎",
            "Semantic Search",
            "Find the most relevant information using vector-based retrieval."
        ),
        (
            "🧠",
            "AI Reasoning",
            "Use LLM to orchestrate retrieval, reasoning, and generation."
        ),
    ]

    columns = st.columns(3)
    for column, (icon, title, description) in zip(
        columns,
        features,
    ):
        with column:
            st.html(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">
                        {icon}
                    </div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """
            )



def _steps_data():
    st.html(
        """
        <div class="section-title">
            <h2>How it works</h2>
            <p>
                From your documents to meaningful answers in four steps.
            </p>
        </div>
        """
    )
    with st.container(border=True):
        columns = st.columns(4)
        steps = [
            (
                "01",
                "Upload/connect",
                "Add your PDF, DOCX,DB or text documents."
            ),
            (
                "02",
                "Index",
                "Convert your documents into searchable embeddings."
            ),
            (
                "03",
                "Retrieve",
                "Find relevant context from your knowledge base."
            ),
            (
                "04",
                "Answer",
                "Generate a grounded response with the LLM."
            ),
        ]
        for column, (number, title, description) in zip(
            columns,
            steps,
        ):
            with column:
                st.html(
                    f"""
                    <div class="step-number">
                        STEP {number}
                    </div>

                    <div class="step-title">
                        {title}
                    </div>

                    <div class="step-description">
                        {description}
                    </div>
                    """
                )


def _redirect_to_chat(agent_page):
    """Redirect user to the chat page."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(
            "💬 Start a conversation",
            use_container_width=True,
            type="primary",
        
        ):
            st.switch_page(
                st.Page(
                    agent,
                    title="Agent",
                    icon=":material/smart_toy:",
                    url_path="agent",
                )
            )


    st.write("")


def _footer():
    st.html(
        """
        <footer class="footer">
            <div class="footer-brand">
                🤖 LLM RAG Assistant
            </div>
            <div class="footer-description">
                Intelligent conversations powered by
                Retrieval-Augmented Generation.
            </div>
            <div class="footer-copy">
                © 2026 LLM RAG Assistant. All rights reserved.
            </div>
        </footer>
        """
    )


def home(agent_page):
    home_css()
    _baner_data()

    st.write("")

    _redirect_to_chat(agent_page)

    _feature_data()
    _steps_data()
    _footer()

    
