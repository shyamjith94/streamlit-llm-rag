import streamlit as st



def home_css():

    st.html(
        """
        <style>

        /* ================================
           PAGE
        ================================= */

        .main .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            max-width: 1200px;
        }

        /* ================================
           HERO
        ================================= */

        .hero {
            position: relative;
            overflow: hidden;

            padding: 18px 30px;
            margin-bottom: 14px;

            border-radius: 22px;
            text-align: center;

            background:
                radial-gradient(
                    circle at 15% 20%,
                    rgba(99, 102, 241, 0.20),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 85% 80%,
                    rgba(139, 92, 246, 0.18),
                    transparent 30%
                ),
                linear-gradient(
                    135deg,
                    #111827,
                    #1e1b4b
                );

            color: white;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
        }

        .hero-icon {
            font-size: 32px;
            margin-bottom: 4px;
        }

        .hero-badge {
            display: inline-block;

            padding: 4px 12px;
            margin-bottom: 8px;

            border: 1px solid rgba(255,255,255,0.20);
            border-radius: 999px;

            background: rgba(255,255,255,0.08);

            font-size: 12px;
            font-weight: 600;
        }

        .hero h1 {
            margin: 0;

            font-size: clamp(30px, 4vw, 44px);
            font-weight: 800;

            letter-spacing: -1px;
        }

        .hero h1 span {
            color: #a5b4fc;
        }

        .hero p {
            max-width: 650px;

            margin: 8px auto 0;

            color: rgba(255,255,255,0.78);

            font-size: 15px;
            line-height: 1.4;
        }

        /* ================================
           SECTION TITLE
        ================================= */

        .section-title {
            text-align: center;

            margin: 30px 0 20px;
        }

        .section-title h2 {
            margin: 20px 0 10px;

            font-size: 22px;
            font-weight: 700;
        }

        .section-title p {
            margin: 0;

            font-size: 20px;
            opacity: 0.60;
        }

        /* ================================
           FEATURE CARDS
        ================================= */

        .feature-card {
            min-height: 130px;

            padding: 16px;

            border: 1px solid rgba(128,128,128,0.20);
            border-radius: 16px;

            background: rgba(128,128,128,0.04);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-3px);

            box-shadow:
                0 8px 20px rgba(0,0,0,0.08);
        }

        .feature-icon {
            width: 38px;
            height: 38px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 10px;

            background: rgba(99,102,241,0.12);

            font-size: 20px;

            margin-bottom: 8px;
        }

        .feature-card h3 {
            margin: 0 0 5px;

            font-size: 16px;
        }

        .feature-card p {
            margin: 0;

            font-size: 12px;
            line-height: 1.4;

            opacity: 0.65;
        }

        /* ================================
           WORKFLOW
        ================================= */

        .workflow {
            padding: 20px;

            border-radius: 16px;

            border: 1px solid rgba(128,128,128,0.18);

            background: rgba(128,128,128,0.035);
        }

        .step-number {
            font-size: 20px;
            font-weight: 700;

            opacity: 0.50;

            margin-bottom: 3px;
        }

        .step-title {
            font-size: 20px;
            font-weight: 700;

            margin-bottom: 5px;
        }

        .step-description {
            font-size: 15px;

            opacity: 0.60;

            line-height: 1.35;
        }

        /* ================================
           STATS
        ================================= */

        .stat {
            text-align: center;

            padding: 8px;
        }

        .stat-value {
            font-size: 22px;
            font-weight: 800;
        }

        .stat-label {
            font-size: 11px;

            opacity: 0.60;

            margin-top: 2px;
        }

        /* ================================
           FOOTER
        ================================= */

        .footer {
            margin-top: 25px;

            padding: 20px 10px 5px;

            border-top:
                1px solid rgba(128,128,128,0.20);

            text-align: center;
        }

        .footer-brand {
            font-size: 14px;
            font-weight: 700;

            margin-bottom: 3px;
        }

        .footer-description {
            font-size: 13px;

            opacity: 0.50;

            margin-bottom: 4px;
        }

        .footer-links {
            font-size: 13px;

            opacity: 0.60;
        }

        .footer-copy {
            margin-top: 5px;

            font-size: 9px;

            opacity: 0.40;
        }

        /* ================================
           STREAMLIT ELEMENT SPACING
        ================================= */

        div[data-testid="stVerticalBlock"] {
            gap: 0.35rem;
        }

        div[data-testid="stHorizontalBlock"] {
            gap: 0.75rem;
        }

        </style>
        """
    )