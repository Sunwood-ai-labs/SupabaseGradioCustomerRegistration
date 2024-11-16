import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap');

        /* Global styles */
        html, body, [class*="css"] {
            font-family: 'Noto Sans JP', sans-serif;
        }

        /* Header styles */
        h1, h2, h3 {
            font-family: 'Noto Sans JP', sans-serif;
            font-weight: 700;
            color: #333333;
            margin-bottom: 1.5rem;
        }

        h1 {
            font-size: 2.5rem;
            border-bottom: 2px solid #4B0082;
            padding-bottom: 0.5rem;
        }

        h3 {
            font-size: 1.5rem;
            color: #4B0082;
            margin-top: 2rem;
        }

        /* Input field styles */
        .stTextInput > label {
            font-size: 1rem;
            font-weight: 500;
            color: #333333;
            margin-bottom: 0.5rem;
        }

        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 1px solid #E0E0E0;
            padding: 0.75rem;
            transition: all 0.3s ease;
        }

        .stTextInput > div > div > input:focus {
            border-color: #4B0082;
            box-shadow: 0 0 0 2px rgba(75, 0, 130, 0.1);
        }

        /* Button styles */
        .stButton > button {
            width: 100%;
            background-color: #4B0082;
            color: white;
            font-weight: 500;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .stButton > button:hover {
            background-color: #3A0065;
            transform: translateY(-1px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        }

        /* Message styles */
        .success-message {
            padding: 1rem 1.5rem;
            border-radius: 8px;
            background-color: #E8F5E9;
            color: #2E7D32;
            margin: 1rem 0;
            border-left: 4px solid #2E7D32;
            font-weight: 500;
        }

        .error-message {
            padding: 1rem 1.5rem;
            border-radius: 8px;
            background-color: #FFF3F3;
            color: #C62828;
            margin: 1rem 0;
            border-left: 4px solid #C62828;
            font-weight: 500;
        }

        /* Customer list styles */
        .element-container:has(p) {
            background-color: #F8F9FA;
            padding: 1rem;
            border-radius: 8px;
            margin: 0.5rem 0;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
        }

        .element-container:has(p):hover {
            transform: translateX(4px);
            border-color: #4B0082;
        }

        /* Info message style */
        .stAlert {
            border-radius: 8px;
            border: none;
            padding: 1rem 1.5rem;
            font-weight: 500;
        }
        </style>
    """, unsafe_allow_html=True)
