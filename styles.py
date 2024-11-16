import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        .stTextInput > label {
            font-size: 16px;
            font-weight: bold;
            color: #1f1f1f;
        }
        .stButton > button {
            width: 100%;
            background-color: #0066cc;
            color: white;
            font-weight: bold;
        }
        .success-message {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #d4edda;
            color: #155724;
            margin: 1rem 0;
        }
        .error-message {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #f8d7da;
            color: #721c24;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
