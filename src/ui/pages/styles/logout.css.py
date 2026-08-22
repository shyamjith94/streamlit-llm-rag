import streamlit as st
def logout_css():
    st.html(
        """
        /* =====================================
   Sidebar Logout
   ===================================== */

.sidebar-logout-wrapper {
    position: fixed;
    bottom: 20px;
    left: 0;
    width: 100%;
    padding: 0 16px;
    box-sizing: border-box;
}


/* Logout button */

.sidebar-logout-wrapper button {
    width: 100% !important;

    background: transparent !important;

    color: #94a3b8 !important;

    border: 1px solid #334155 !important;

    border-radius: 10px !important;

    padding: 10px 12px !important;

    font-size: 14px !important;

    font-weight: 550 !important;

    transition:
        background 0.18s ease,
        color 0.18s ease,
        border-color 0.18s ease;
}


/* Hover */

.sidebar-logout-wrapper button:hover {
    background: #1e293b !important;

    color: #ffffff !important;

    border-color: #475569 !important;
}
        """
    )
