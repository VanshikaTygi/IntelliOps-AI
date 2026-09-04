import streamlit as st

def load_custom_css():
    st.markdown("""
        <style>
        .hero-banner {
            background: linear-gradient(135deg, #16213E 0%, #0F3460 100%);
            border-left: 4px solid #4A9EFF;
            padding: 24px 28px;
            border-radius: 8px;
            margin-bottom: 24px;
        }
        .hero-banner h1 {
            margin: 0;
            font-size: 28px;
            color: #FFFFFF;
        }
        .hero-banner p {
            color: #B8C4D9;
            margin-top: 8px;
            font-size: 15px;
        }
        .status-card {
            background-color: #16213E;
            color: #E2E8F0;
            border-radius: 8px;
            padding: 16px 20px;
            border: 1px solid #2A3F66;
            margin-bottom: 12px;
            line-height: 1.6;
        }
        .agent-tag {
            display: inline-block;
            background-color: #4A9EFF22;
            color: #4A9EFF;
            border: 1px solid #4A9EFF;
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 13px;
            font-weight: 600;
            margin-right: 8px;
        }
        .metric-box {
            background: linear-gradient(135deg, #16213E 0%, #1A2847 100%);
            border-radius: 8px;
            padding: 18px;
            text-align: center;
            border: 1px solid #2A3F66;
        }
        .metric-box h2 {
            margin: 0;
            color: #4A9EFF;
            font-size: 32px;
        }
        .metric-box p {
            margin: 4px 0 0 0;
            color: #B8C4D9;
            font-size: 13px;
        }
        </style>
    """, unsafe_allow_html=True)