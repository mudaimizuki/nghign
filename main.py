import streamlit as st
import time

# Cấu hình trang - Giao diện rộng rãi để làm game
st.set_page_config(page_title="Usagi: Sinh Tồn Nơi Rừng Sâu", layout="centered", page_icon="🐰")

# ====================== CSS ĐỈNH CHÓP - PHONG CÁCH RPG ======================
st.markdown("""
<style>
    /* Nền game: Rừng sâu thăm thẳm */
    .stApp {
        background: radial-gradient(circle at center, #1b3a26 0%, #0d1e13 60%, #050a06 100%);
        color: #f0f4f1;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Khung Header RPG */
    .rpg-header {
        background: linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(20, 50, 20, 0.8) 50%, rgba(0,0,0,0) 100%);
        border-top: 2px solid #d4af37;
        border-bottom: 2px solid #d4af37;
        text-align: center;
        padding: 20px;
        margin-bottom: 30px;
        text-shadow: 0 0 10px #d4af37;
    }

    /* Bảng câu hỏi - Giống cuộn giấy da */
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

    /* Nút bấm (Lựa chọn) */
    .stButton>button {
        background: linear-
