import os
import streamlit as st
from supabase import create_client, Client
from datetime import datetime
from styles import apply_custom_styles
from utils import validate_email, validate_phone, validate_required, format_customer_info

# Supabaseの設定
supabase: Client = None
try:
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

    if not SUPABASE_URL or not SUPABASE_KEY:
        st.error("Supabase configuration is missing. Please check your environment variables.")
    else:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    st.error(f"Failed to initialize Supabase client: {str(e)}")

def init_session_state():
    if 'show_success' not in st.session_state:
        st.session_state.show_success = False
    if 'success_message' not in st.session_state:
        st.session_state.success_message = ""
    if 'error_message' not in st.session_state:
        st.session_state.error_message = ""

def clear_form():
    st.session_state.last_name = ""
    st.session_state.first_name = ""
    st.session_state.email = ""
    st.session_state.phone = ""
    st.session_state.address = ""

def add_customer():
    if not supabase:
        st.error("データベース接続が確立されていません。")
        return

    # フォームのバリデーション
    is_valid = True
    error_messages = []
    
    last_name_valid, last_name_error = validate_required(
        st.session_state.last_name, "姓")
    if not last_name_valid:
        is_valid = False
        error_messages.append(last_name_error)
    
    first_name_valid, first_name_error = validate_required(
        st.session_state.first_name, "名")
    if not first_name_valid:
        is_valid = False
        error_messages.append(first_name_error)
    
    email_valid, email_error = validate_email(st.session_state.email)
    if not email_valid:
        is_valid = False
        error_messages.append(email_error)
    
    phone_valid, phone_error = validate_phone(st.session_state.phone)
    if not phone_valid:
        is_valid = False
        error_messages.append(phone_error)

    if not is_valid:
        st.session_state.error_message = "\n".join(error_messages)
        st.session_state.show_success = False
        return

    try:
        customer_data = {
            "last_name": st.session_state.last_name,
            "first_name": st.session_state.first_name,
            "email": st.session_state.email,
            "phone": st.session_state.phone,
            "address": st.session_state.address
        }

        supabase.table("customers").insert(customer_data).execute()
        
        st.session_state.show_success = True
        st.session_state.success_message = "顧客情報が正常に登録されました。"
        st.session_state.error_message = ""
        clear_form()
        
    except Exception as e:
        st.session_state.error_message = f"エラーが発生しました: {str(e)}"
        st.session_state.show_success = False

def main():
    apply_custom_styles()
    init_session_state()

    st.title("顧客管理システム")
    st.markdown("### 新規顧客登録")

    # フォーム
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("姓", key="last_name", placeholder="山田")
    with col2:
        st.text_input("名", key="first_name", placeholder="太郎")
    
    st.text_input("メールアドレス", key="email", placeholder="example@email.com")
    st.text_input("電話番号（任意）", key="phone", placeholder="090-1234-5678")
    st.text_input("住所（任意）", key="address", placeholder="東京都渋谷区...")

    st.button("登録", on_click=add_customer, type="primary")

    # メッセージの表示
    if st.session_state.show_success:
        st.markdown(f'<div class="success-message">{st.session_state.success_message}</div>',
                   unsafe_allow_html=True)
    if st.session_state.error_message:
        st.markdown(f'<div class="error-message">{st.session_state.error_message}</div>',
                   unsafe_allow_html=True)

    # 顧客一覧の表示
    st.markdown("### 登録済み顧客一覧")
    if not supabase:
        st.error("データベース接続が確立されていません。")
        return

    try:
        result = supabase.table("customers") \
            .select("*") \
            .order("created_at", desc=True) \
            .execute()
        
        if result.data:
            for customer in result.data:
                st.markdown(f"- {format_customer_info(customer)}")
        else:
            st.info("登録済みの顧客はいません。")
            
    except Exception as e:
        st.error(f"顧客データの取得中にエラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()
