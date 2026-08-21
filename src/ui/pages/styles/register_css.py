import streamlit as st


def register_css():
    st.html(
        """
        <style>

        /* =========================
           Page
        ========================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(99, 102, 241, 0.10),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 90%,
                    rgba(168, 85, 247, 0.10),
                    transparent 30%
                ),
                #f8fafc;
        }

        .block-container {
            width: 100%;
            max-width: 520px;
            margin: 0 auto;
            padding: 7vh 20px 5vh 20px;
            box-sizing: border-box;
        }


        /* =========================
           Register Card
           ========================= */

        .register-card {
            width: 100%;
            box-sizing: border-box;
            height: auto;
            min-height: 0;
            background: rgba(255, 255, 255, 0.96);
            border: 1px solid rgba(226, 232, 240, 0.9);
            border-radius: 24px;
            padding: 36px 38px 32px;

            box-shadow:
                0 20px 50px rgba(15, 23, 42, 0.08),
                0 4px 12px rgba(15, 23, 42, 0.04);
        }


        /* =========================
           Logo
           ========================= */

        .register-logo {
            width: 58px;
            height: 58px;
            margin: 0 auto 20px auto;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 17px;

            background: linear-gradient(
                135deg,
                #6366f1,
                #8b5cf6
            );

            color: white;
            font-size: 27px;

            box-shadow:
                0 10px 25px rgba(99, 102, 241, 0.25);
        }


        /* =========================
           Heading
           ========================= */

        .register-title {
            text-align: center;
            font-size: 30px;
            line-height: 1.2;
            font-weight: 750;
            letter-spacing: -0.7px;
            color: #0f172a;
            margin-bottom: 8px;
        }

        .register-subtitle {
            text-align: center;
            font-size: 14px;
            line-height: 1.6;
            color: #64748b;
            margin-bottom: 28px;
        }

         /* =========================
           Form 
           ========================= */
        div[data-testid="stForm"] {
            width: 100% !important;
            max-width: 100% !important;
        }


        /* =========================
           Form labels
           ========================= */

        div[data-testid="stTextInput"] label {
            font-size: 13px !important;
            font-weight: 600 !important;
            color: #334155 !important;
        }


        /* =========================
           Inputs
           ========================= */

        div[data-testid="stTextInput"] input {
            height: 46px !important;
            border-radius: 11px !important;

            border: 1px solid #e2e8f0 !important;

            background: #f8fafc !important;

            padding-left: 14px !important;
            padding-right: 14px !important;

            font-size: 14px !important;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease,
                background 0.2s ease;
        }

        div[data-testid="stTextInput"] input:hover {
            border-color: #cbd5e1 !important;
            background: #ffffff !important;
        }

        div[data-testid="stTextInput"] input:focus {
            border-color: #6366f1 !important;
            background: #ffffff !important;

            box-shadow:
                0 0 0 3px rgba(99, 102, 241, 0.12) !important;
        }


        /* =========================
           Form spacing
           ========================= */

        div[data-testid="stTextInput"] {
            margin-bottom: 8px;
        }


        /* =========================
           Submit Button
           ========================= */

        div.stFormSubmitButton > button {
            height: 48px !important;

            border-radius: 12px !important;

            border: none !important;

            background:
                linear-gradient(
                    135deg,
                    #6366f1,
                    #7c3aed
                ) !important;

            color: white !important;

            font-size: 15px !important;
            font-weight: 650 !important;

            box-shadow:
                0 8px 20px rgba(99, 102, 241, 0.25);

            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease;
        }

        div.stFormSubmitButton > button:hover {
            transform: translateY(-1px);

            box-shadow:
                0 12px 25px rgba(99, 102, 241, 0.30);
        }

        div.stFormSubmitButton > button:active {
            transform: translateY(0);
        }


        /* =========================
           Password Hint
           ========================= */

        .password-hint {
            font-size: 12px;
            color: #94a3b8;
            margin-top: -2px;
            margin-bottom: 12px;
        }


        /* =========================
           Divider
           ========================= */

        .register-divider {
            display: flex;
            align-items: center;
            gap: 12px;

            margin: 22px 0;

            color: #94a3b8;
            font-size: 12px;
        }

        .register-divider::before,
        .register-divider::after {
            content: "";
            height: 1px;
            flex: 1;
            background: #e2e8f0;
        }


        /* =========================
           Login Link
           ========================= */

        .login-text {
            text-align: center;

            color: #64748b;

            font-size: 13px;

            margin-top: 22px;
        }

        .login-link {
            color: #6366f1;
            font-weight: 650;
            text-decoration: none;
        }

        .login-link:hover {
            text-decoration: underline;
        }


        /* =========================
           Footer
           ========================= */

        .register-footer {
            text-align: center;

            margin-top: 22px;

            color: #94a3b8;

            font-size: 11px;
        }


        /* =========================
           Mobile
           ========================= */

        @media (max-width: 600px) {

            .block-container {
                padding-left: 18px;
                padding-right: 18px;
                padding-top: 4vh;
            }

            .register-card {
                padding: 30px 22px 26px 22px;
                border-radius: 20px;
            }

            .register-title {
                font-size: 27px;
            }
        }

        </style>
        """
    )
