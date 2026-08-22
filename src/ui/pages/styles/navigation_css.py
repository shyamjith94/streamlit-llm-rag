import streamlit as st

def navigation_css():
    st.html(
        """
        <style>

        /* =====================================================
           DESIGN TOKENS
           ===================================================== */

        :root {
            --app-bg: #f5f7fb;
            --sidebar-bg: #f8fafc;
            --card-bg: #ffffff;

            --text-primary: #172033;
            --text-secondary: #64748b;
            --text-muted: #94a3b8;

            --border: #e5e7eb;
            --border-light: #edf0f4;

            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --primary-soft: #eef2ff;

            --hover: #f1f5f9;
        }


        /* =====================================================
           ENTIRE STREAMLIT APP
           ===================================================== */

        html,
        body,
        .stApp {
            background: var(--app-bg) !important;
            background-color: var(--app-bg) !important;

            color: var(--text-primary);
        }


        /* =====================================================
           MAIN CONTENT
           ===================================================== */

        .main {
            background: var(--app-bg) !important;
        }

        .block-container {
            background: transparent !important;
        }


        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {
            background: var(--sidebar-bg) !important;
            background-color: var(--sidebar-bg) !important;

            border-right: 1px solid var(--border) !important;

            box-shadow: none !important;
        }

        section[data-testid="stSidebar"] > div {
            background: var(--sidebar-bg) !important;
        }

        section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
            background: var(--sidebar-bg) !important;
        }


        /* =====================================================
           SIDEBAR BRAND
           ===================================================== */

        .navigation-brand {
            display: flex;

            align-items: center;

            gap: 11px;

            padding: 6px 10px 20px;

            margin-bottom: 10px;

            border-bottom: 1px solid var(--border-light);
        }

        .navigation-logo {
            width: 38px;
            height: 38px;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 11px;

            background: var(--primary-soft);

            color: var(--primary);

            font-size: 18px;

            box-shadow:
                0 4px 12px rgba(99, 102, 241, 0.08);
        }

        .navigation-brand-name {
            color: var(--text-primary);

            font-size: 16px;

            font-weight: 700;

            letter-spacing: -0.3px;
        }

        .navigation-brand-subtitle {
            color: var(--text-muted);

            font-size: 10px;

            margin-top: 2px;
        }


        /* =====================================================
           NATIVE STREAMLIT NAVIGATION
           ===================================================== */

        section[data-testid="stSidebarNav"] {
            background: transparent !important;

            padding: 0 5px !important;
        }

        section[data-testid="stSidebarNav"] > ul {
            background: transparent !important;

            padding: 0 !important;
        }

        section[data-testid="stSidebarNav"] li {
            background: transparent !important;

            margin: 3px 0 !important;
        }


        /* Navigation links */

        section[data-testid="stSidebarNav"] li a {
            min-height: 42px;

            display: flex;

            align-items: center;

            padding: 0 12px !important;

            border-radius: 10px !important;

            background: transparent !important;

            color: var(--text-secondary) !important;

            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif !important;

            font-size: 13.5px !important;

            font-weight: 500 !important;

            transition:
                background 0.15s ease,
                color 0.15s ease;
        }


        /* Navigation hover */

        section[data-testid="stSidebarNav"] li a:hover {
            background: var(--hover) !important;

            color: var(--text-primary) !important;
        }


        /* Active navigation */

        section[data-testid="stSidebarNav"]
        li a[aria-current="page"] {

            background: var(--primary-soft) !important;

            color: var(--primary-dark) !important;

            border: 1px solid #e0e7ff !important;

            font-weight: 600 !important;
        }


        /* =====================================================
           NAVIGATION SECTION HEADERS
           ===================================================== */

        section[data-testid="stSidebarNav"]
        [data-testid="stSidebarNavSectionHeader"] {

            background: transparent !important;

            color: var(--text-muted) !important;

            font-size: 10px !important;

            font-weight: 700 !important;

            text-transform: uppercase;

            letter-spacing: 0.8px;

            padding: 15px 12px 6px !important;
        }


        /* =====================================================
           LOGIN / REGISTER PAGE AREA
           ===================================================== */

        .auth-page {
            min-height: calc(100vh - 40px);

            display: flex;

            flex-direction: column;

            align-items: center;

            justify-content: center;

            padding: 40px 20px;
        }


        /* =====================================================
           AUTH HEADER
           ===================================================== */

        .auth-logo {
            width: 60px;
            height: 60px;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 17px;

            background: var(--primary-soft);

            color: var(--primary);

            font-size: 27px;

            margin-bottom: 18px;

            box-shadow:
                0 8px 20px
                rgba(99, 102, 241, 0.10);
        }

        .auth-title {
            color: var(--text-primary);

            font-size: 30px;

            line-height: 1.2;

            font-weight: 750;

            letter-spacing: -0.8px;

            margin-bottom: 7px;

            text-align: center;
        }

        .auth-subtitle {
            color: var(--text-secondary);

            font-size: 14px;

            line-height: 1.5;

            text-align: center;

            margin-bottom: 28px;
        }


        /* =====================================================
           AUTH FORM
           ===================================================== */

        div[data-testid="stForm"] {

            width: 100%;

            max-width: 440px;

            background: var(--card-bg) !important;

            border: 1px solid var(--border) !important;

            border-radius: 18px !important;

            padding: 32px 36px 30px !important;

            box-shadow:
                0 12px 35px
                rgba(15, 23, 42, 0.06),

                0 2px 8px
                rgba(15, 23, 42, 0.03) !important;
        }


        /* =====================================================
           INPUT LABELS
           ===================================================== */

        div[data-testid="stTextInput"] label {

            color: #334155 !important;

            font-size: 13px !important;

            font-weight: 600 !important;
        }


        /* =====================================================
           INPUTS
           ===================================================== */

        div[data-testid="stTextInput"] input {

            height: 46px !important;

            background: #f8fafc !important;

            color: var(--text-primary) !important;

            border: 1px solid #e2e8f0 !important;

            border-radius: 10px !important;

            font-size: 14px !important;

            padding: 0 13px !important;

            transition:
                border 0.15s ease,
                box-shadow 0.15s ease,
                background 0.15s ease;
        }


        /* Input hover */

        div[data-testid="stTextInput"] input:hover {

            background: #ffffff !important;

            border-color: #cbd5e1 !important;
        }


        /* Input focus */

        div[data-testid="stTextInput"] input:focus {

            background: #ffffff !important;

            border-color: var(--primary) !important;

            box-shadow:
                0 0 0 3px
                rgba(99, 102, 241, 0.10) !important;
        }


        /* Placeholder */

        div[data-testid="stTextInput"] input::placeholder {

            color: #9ca3af !important;
        }


        /* =====================================================
           FORM SUBMIT BUTTON
           ===================================================== */

        div.stFormSubmitButton > button {

            height: 47px !important;

            border: none !important;

            border-radius: 10px !important;

            background:
                linear-gradient(
                    135deg,
                    #6366f1,
                    #7c3aed
                ) !important;

            color: #ffffff !important;

            font-size: 14px !important;

            font-weight: 600 !important;

            box-shadow:
                0 8px 18px
                rgba(99, 102, 241, 0.20) !important;

            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease;
        }

        div.stFormSubmitButton > button:hover {

            transform: translateY(-1px);

            box-shadow:
                0 10px 24px
                rgba(99, 102, 241, 0.25) !important;
        }


        /* =====================================================
           FORGOT PASSWORD
           ===================================================== */

        .forgot-password {

            text-align: right;

            margin-top: -2px;

            margin-bottom: 20px;

            font-size: 12px;
        }

        .forgot-password a {

            color: var(--primary);

            font-weight: 600;

            text-decoration: none;
        }

        .forgot-password a:hover {
            color: var(--primary-dark);

            text-decoration: underline;
        }


        /* =====================================================
           AUTH FOOTER
           ===================================================== */

        .auth-register {

            margin-top: 20px;

            color: var(--text-secondary);

            font-size: 13px;

            text-align: center;
        }

        .auth-register a {

            color: var(--primary);

            font-weight: 600;

            text-decoration: none;
        }

        .auth-register a:hover {
            text-decoration: underline;
        }

        .auth-footer {

            margin-top: 14px;

            color: var(--text-muted);

            font-size: 11px;

            text-align: center;
        }


        /* =====================================================
           REMOVE UNNECESSARY TOP SPACE
           ===================================================== */

        header[data-testid="stHeader"] {
            background: transparent !important;
        }


        /* =====================================================
           MOBILE
           ===================================================== */

        @media (max-width: 700px) {

            div[data-testid="stForm"] {

                max-width: 100%;

                padding:
                    28px 22px 26px !important;
            }

            .auth-title {
                font-size: 27px;
            }

            .auth-page {
                padding:
                    25px 15px;
            }
        }

        </style>
        """
    )
    st.html(
        """
        <style>

        /* =====================================================
           STREAMLIT SIDEBAR - FORCE WHITE
           ===================================================== */

        section[data-testid="stSidebar"],
        section[data-testid="stSidebar"] > div,
        section[data-testid="stSidebar"] > div > div,
        section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
            background: #ffffff !important;
            background-color: #ffffff !important;
        }


        /* =====================================================
           NATIVE STREAMLIT NAVIGATION
           ===================================================== */

        section[data-testid="stSidebarNav"] {
            background: #ffffff !important;
            background-color: #ffffff !important;

            padding: 0 8px !important;
        }

        section[data-testid="stSidebarNav"] > ul {
            background: #ffffff !important;
            background-color: #ffffff !important;

            padding: 0 !important;
        }


        /* Navigation list items */

        section[data-testid="stSidebarNav"] li {
            background: #ffffff !important;
            background-color: #ffffff !important;

            margin: 3px 0 !important;
        }


        /* Navigation links */

        section[data-testid="stSidebarNav"] li a {
            background: #ffffff !important;
            background-color: #ffffff !important;

            color: #64748b !important;

            border-radius: 9px !important;

            padding: 10px 12px !important;

            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif !important;

            font-size: 14px !important;

            font-weight: 500 !important;

            transition:
                background-color 0.15s ease,
                color 0.15s ease;
        }


        /* =====================================================
           HOVER
           ===================================================== */

        section[data-testid="stSidebarNav"] li a:hover {
            background: #f8fafc !important;
            background-color: #f8fafc !important;

            color: #334155 !important;
        }


        /* =====================================================
           ACTIVE PAGE
           ===================================================== */

        section[data-testid="stSidebarNav"]
        li a[aria-current="page"] {

            background: #eef2ff !important;
            background-color: #eef2ff !important;

            color: #4f46e5 !important;

            border: 1px solid #e0e7ff !important;

            font-weight: 600 !important;
        }


        /* =====================================================
           ACTIVE PAGE HOVER
           ===================================================== */

        section[data-testid="stSidebarNav"]
        li a[aria-current="page"]:hover {

            background: #e0e7ff !important;
            background-color: #e0e7ff !important;

            color: #4338ca !important;
        }


        /* =====================================================
           NAVIGATION SECTION HEADERS
           ===================================================== */

        section[data-testid="stSidebarNav"]
        [data-testid="stSidebarNavSectionHeader"] {

            background: #ffffff !important;

            color: #94a3b8 !important;

            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif !important;

            font-size: 10px !important;

            font-weight: 700 !important;

            text-transform: uppercase;

            letter-spacing: 0.8px;
        }


        /* =====================================================
           BRAND
           ===================================================== */

        .navigation-brand {
            display: flex;

            align-items: center;

            gap: 11px;

            padding: 4px 10px 20px;

            margin-bottom: 10px;

            background: #ffffff;

            border-bottom: 1px solid #f1f5f9;
        }

        .navigation-logo {
            width: 38px;
            height: 38px;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 10px;

            background: #eef2ff;

            color: #4f46e5;

            font-size: 18px;

            font-weight: 700;
        }

        .navigation-brand-name {
            color: #111827;

            font-size: 16px;

            font-weight: 700;

            letter-spacing: -0.2px;
        }

        .navigation-brand-subtitle {
            color: #94a3b8;

            font-size: 10px;

            font-weight: 400;

            margin-top: 2px;
        }


        /* =====================================================
           SIDEBAR BORDER
           ===================================================== */

        section[data-testid="stSidebar"] {
            border-right: 1px solid #e5e7eb !important;
        }


        /* =====================================================
           SIDEBAR HEADER
           ===================================================== */

        section[data-testid="stSidebar"]
        button[kind="header"] {

            color: #64748b !important;

            background: #ffffff !important;
        }

        section[data-testid="stSidebar"]
        button[kind="header"]:hover {

            background: #f8fafc !important;

            color: #111827 !important;
        }

        </style>
        """
    )
    st.html(
        """
        <style>

        /* =====================================
           Navigation Sidebar
           ===================================== */

        section[data-testid="stSidebar"] {
            background: #0f172a;
            border-right: 1px solid #1e293b;
        }

        section[data-testid="stSidebar"] > div {
            background: #0f172a;
        }

        section[data-testid="stSidebar"] .block-container {
            padding: 20px 12px;
        }


        /* =====================================
           Navigation Items
           ===================================== */

        section[data-testid="stSidebarNav"] {
            padding: 0 4px;
        }

        section[data-testid="stSidebarNav"] ul {
            padding-top: 10px;
        }

        section[data-testid="stSidebarNav"] li {
            margin: 4px 0;
        }


        /* Navigation links */

        section[data-testid="stSidebarNav"] a {
            border-radius: 10px;

            padding: 10px 12px !important;

            color: #94a3b8 !important;

            font-size: 14px !important;

            font-weight: 550 !important;

            transition:
                background 0.18s ease,
                color 0.18s ease,
                transform 0.18s ease;
        }


        /* Hover */

        section[data-testid="stSidebarNav"] a:hover {
            background: #1e293b !important;

            color: #f8fafc !important;

            transform: translateX(2px);
        }


        /* Active page */

        section[data-testid="stSidebarNav"] a[aria-current="page"] {
            background:
                linear-gradient(
                    90deg,
                    rgba(99, 102, 241, 0.22),
                    rgba(124, 58, 237, 0.12)
                ) !important;

            color: #ffffff !important;

            border: 1px solid
                rgba(99, 102, 241, 0.25);
        }


        /* Active icon */

        section[data-testid="stSidebarNav"]
        a[aria-current="page"] span {
            color: #a5b4fc !important;
        }


        /* =====================================
           Navigation Section Headers
           ===================================== */

        section[data-testid="stSidebarNav"] div[data-testid="stSidebarNavSectionHeader"] {
            color: #64748b !important;

            font-size: 10px !important;

            font-weight: 700 !important;

            text-transform: uppercase;

            letter-spacing: 0.8px;

            padding: 12px 12px 5px;
        }


        /* =====================================
           Sidebar Collapse Button
           ===================================== */

        section[data-testid="stSidebar"] button[kind="header"] {
            color: #94a3b8 !important;
        }

        section[data-testid="stSidebar"] button[kind="header"]:hover {
            color: #ffffff !important;
        }


        /* =====================================
           Logo / Brand
           ===================================== */

        .navigation-brand {
            display: flex;

            align-items: center;

            gap: 10px;

            padding: 5px 10px 20px;

            margin-bottom: 8px;

            border-bottom: 1px solid #1e293b;
        }

        .navigation-logo {
            width: 38px;
            height: 38px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 11px;

            background:
                linear-gradient(
                    135deg,
                    #6366f1,
                    #7c3aed
                );

            color: white;

            font-size: 19px;

            box-shadow:
                0 6px 16px
                rgba(99, 102, 241, 0.25);
        }

        .navigation-brand-name {
            color: #f8fafc;

            font-size: 16px;

            font-weight: 700;
        }

        .navigation-brand-subtitle {
            color: #64748b;

            font-size: 10px;

            margin-top: 2px;
        }


        /* =====================================
           Mobile
           ===================================== */

        @media (max-width: 768px) {

            section[data-testid="stSidebarNav"] a {
                padding: 11px 12px !important;
            }

        }

         /* =====================================
       Logout - Bottom of Sidebar
       ===================================== */

        </style>
        """
    )