import streamlit as st

def chat_css():
    st.html(
        """
        <style>

        /* Main container */
        .main .block-container {
            max-width: 1000px;
            padding-top: 1rem;
            padding-bottom: 5rem;
        }

        /* Header */
        .chat-header {
            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 14px 20px;
            margin-bottom: 20px;

            border: 1px solid rgba(128,128,128,0.18);
            border-radius: 16px;

            background: rgba(128,128,128,0.05);
        }

        .chat-header-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .chat-logo {
            width: 42px;
            height: 42px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 12px;

            background: linear-gradient(
                135deg,
                #6366f1,
                #8b5cf6
            );

            font-size: 22px;
        }

        .chat-title {
            font-size: 17px;
            font-weight: 700;
        }

        .chat-subtitle {
            font-size: 12px;
            opacity: 0.55;
            margin-top: 2px;
        }

        .online-status {
            display: flex;
            align-items: center;
            gap: 6px;

            font-size: 12px;
            opacity: 0.65;
        }

        .online-dot {
            width: 8px;
            height: 8px;

            border-radius: 50%;

            background: #22c55e;
        }

        /* Welcome */
        .welcome {
            text-align: center;
            padding: 45px 20px 30px;
        }

        .welcome-icon {
            font-size: 52px;
            margin-bottom: 12px;
        }

        .welcome h1 {
            margin: 0;
            font-size: 30px;
            font-weight: 750;
        }

        .welcome p {
            margin-top: 10px;
            opacity: 0.6;
            font-size: 15px;
        }

        /* Message cards */
        .message-card {
            padding: 18px 20px;
            margin: 12px 0;

            border-radius: 18px;

            border: 1px solid rgba(128,128,128,0.15);
        }

        .user-message {
            background: rgba(99,102,241,0.08);
        }

        .assistant-message {
            background: rgba(128,128,128,0.04);
        }

        .message-header {
            display: flex;
            align-items: center;
            gap: 8px;

            margin-bottom: 8px;

            font-size: 13px;
            font-weight: 700;
        }

        .message-content {
            font-size: 15px;
            line-height: 1.7;
        }

        /* Sources */
        .sources {
            margin-top: 15px;
            padding-top: 12px;

            border-top: 1px solid rgba(128,128,128,0.15);

            font-size: 12px;
            opacity: 0.7;
        }

        .source-item {
            display: inline-block;

            margin: 4px 5px 0 0;
            padding: 5px 9px;

            border-radius: 8px;

            background: rgba(128,128,128,0.08);
        }

        /* Empty state suggestions */
        .suggestion {
            padding: 14px 16px;

            border: 1px solid rgba(128,128,128,0.15);
            border-radius: 12px;

            background: rgba(128,128,128,0.035);

            cursor: pointer;

            font-size: 13px;
        }

        /* Footer */
        .chat-footer {
            text-align: center;

            margin-top: 25px;

            font-size: 11px;
            opacity: 0.4;
        }

        </style>
        """,
    )