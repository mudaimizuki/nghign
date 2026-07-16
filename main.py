import streamlit as st
import time

# ====================== CẤU HÌNH & TƯƠNG THÍCH ======================
st.set_page_config(page_title="Usagi: Sinh Tồn Nơi Rừng Sâu", layout="centered", page_icon="🐰")

# Hàm chống lỗi cho các phiên bản Streamlit cũ
def safe_rerun():
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()

# ====================== CSS ĐỈNH CHÓP - PHONG CÁCH RPG ======================
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at center, #1b3a26 0%, #0d1e13 60%, #050a06 100%);
        color: #f0f4f1;
        font-family: 'Courier New', Courier, monospace;
    }
    .rpg-header {
        background: linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(20, 50, 20, 0.8) 50%, rgba(0,0,0,0) 100%);
        border-top: 2px solid #d4af37;
        border-bottom: 2px solid #d4af37;
        text-align: center;
        padding: 20px;
        margin-bottom: 30px;
        text-shadow: 0 0 10px #d4af37;
    }
    .quest-box {
        background: url('https://www.transparenttextures.com/patterns/aged-paper.png'), linear-gradient(135deg, #e8dcc7, #c9b48f);
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8), inset 0 0 20px rgba(100,60,20,0.5);
        border: 4px solid #5c3a21;
        color: #3b2313;
        font-size: 22px;
        font-weight: 900;
        margin: 20px 0;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(to bottom, #4a6c42, #294023);
        color: #e0d0a6;
        font-size: 18px;
        font-weight: bold;
        height: 75px;
        width: 100%;
        border-radius: 8px;
        border: 2px solid #d4af37;
        box-shadow: 0 6px 0 #121e10, 0 10px 20px rgba(0,0,0,0.6);
        transition: all 0.1s;
        text-transform: uppercase;
    }
    .stButton>button:active {
        transform: translateY(6px);
        box-shadow: 0 0px 0 #121e10, 0 5px 10px rgba(0,0,0,0.6);
    }
    .stButton>button:hover {
        background: linear-gradient(to bottom, #5c8552, #395931);
        color: #ffffff;
        border-color: #ffea00;
        box-shadow: 0 6px 0 #121e10, 0 0 25px rgba(212, 175, 55, 0.6);
    }
    .timer-danger {
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        color: #ff3333;
        text-shadow: 0 0 15px #ff0000, 0 0 30px #8b0000;
        background: rgba(0, 0, 0, 0.6);
        border: 3px solid #ff3333;
        border-radius: 50%;
        width: 120px;
        height: 120px;
        line-height: 110px;
        margin: 0 auto 20px auto;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);
    }
    .scene-text {
        font-size: 20px;
        text-align: center;
        padding: 15px;
        background: rgba(0, 0, 0, 0.5);
        border-left: 5px solid #4caf50;
        color: #a5d6a7;
        font-style: italic;
        margin-bottom: 20px;
    }
    .feedback-correct {
        color: #00ffcc; text-align: center; font-size: 30px; font-weight: bold; text-shadow: 0 0 20px #00ffcc; margin-top: 15px;
    }
    .feedback-wrong {
        color: #ff3333; text-align: center; font-size: 30px; font-weight: bold; text-shadow: 0 0 20px #ff0000; margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ====================== DỮ LIỆU GAME ======================
questions = [
    {"q": "Kí hiệu nào dưới đây dùng để viết tổ hợp chập 4 của 8 phần tử?", "options": ["A. C(8,4)", "B. C(4,8)", "C. A(8,4)", "D. A(4,8)"], "answer": 0},
    # Đã sửa lại câu 2 theo
