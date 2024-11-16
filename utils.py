import re
from typing import Tuple, Optional

def validate_email(email: str) -> Tuple[bool, Optional[str]]:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        return False, "メールアドレスは必須項目です。"
    if not re.match(pattern, email):
        return False, "有効なメールアドレスを入力してください。"
    return True, None

def validate_phone(phone: str) -> Tuple[bool, Optional[str]]:
    if not phone:
        return True, None
    pattern = r'^(0\d{1,4}-\d{1,4}-\d{4}|\d{10,11})$'
    if not re.match(pattern, phone):
        return False, "電話番号の形式が正しくありません。"
    return True, None

def validate_required(value: str, field_name: str) -> Tuple[bool, Optional[str]]:
    if not value:
        return False, f"{field_name}は必須項目です。"
    return True, None

def format_customer_info(customer: dict) -> str:
    name = f"{customer['last_name']} {customer['first_name']}"
    info = [f"{name} 様"]
    info.append(f"メール: {customer['email']}")
    
    if customer['phone']:
        info.append(f"電話: {customer['phone']}")
    if customer['address']:
        info.append(f"住所: {customer['address']}")
    
    created_at = customer['created_at'].split('T')[0]  # YYYY-MM-DD形式に変換
    info.append(f"登録日: {created_at}")
    
    return " | ".join(info)
