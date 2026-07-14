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
    {"q": "Khai triển biểu thức x²(3x-2)⁵ ta nhận được bao nhiêu số hạng?", "options": ["A. 6", "B. 5", "C. 7", "D. 8"], "answer": 2},
    {"q": "Một hộp chứa 12 sản phẩm tốt và 4 sản phẩm kém chất lượng, rút ngẫu nhiên 3 sản phẩm. Số phần tử của không gian mẫu là?", "options": ["A. 560", "B. 220", "C. 364", "D. 455"], "answer": 0},
    {"q": "Số cách chọn 2 học sinh từ 5 học sinh là", "options": ["A. C(5,2)", "B. A(5,2)", "C. C(2,5)", "D. A(2,5)"], "answer": 0},
    {"q": "Số hạng không chứa x trong khai triển (√x - 3/x)³ là", "options": ["A. 2⁵", "B. C(2,5)", "C. A(2,5)", "D. -27"], "answer": 3},
    {"q": "Cho phép thử ngẫu nhiên. Phát biểu nào sau đây là đúng?", "options": ["A. Mọi kết quả đều có xác suất bằng nhau", "B. Không gian mẫu là vô hạn", "C. Biến cố là tập con của không gian mẫu", "D. Cả A và C"], "answer": 3},
    {"q": "Trong không gian mẫu, biến cố chắc chắn là biến cố như thế nào?", "options": ["A. Là biến cố có xác suất bằng 0.", "B. Là biến cố luôn xảy ra khi thực hiện phép thử.", "C. Là biến cố không bao giờ xảy ra.", "D. Là biến cố chỉ có một kết quả duy nhất."], "answer": 1},
    {"q": "Phương trình tổng quát của đường thẳng có dạng là:", "options": ["A. ax² + by + c = 0.", "B. y = ax + b.", "C. ax + by + c = 0 (với a² + b² > 0).", "D. x = x₀ + at; y = y₀ + bt."], "answer": 2},
    {"q": "Phát biểu nào sau đây là đúng về hai đường thẳng song song trong mặt phẳng?", "options": ["A. Hai đường thẳng song song là hai đường thẳng có vectơ pháp tuyến cùng phương.", "B. Hai đường thẳng song song là hai đường thẳng có vectơ chỉ phương cùng phương.", "C. Hai đường thẳng song song không bao giờ có cùng hệ số góc.", "D. Hai đường thẳng song song cắt nhau tại một điểm."], "answer": 1},
    {"q": "Trong mặt phẳng Oxy, phương trình nào sau đây là phương trình chính tắc của một đường tròn?", "options": ["A. x² + y² = -4", "B. x² + y² = 0", "C. x² - y² = 4", "D. x² + y² = 4"], "answer": 3}
]

scenes = [
    "🌲 Ải 1: Bìa rừng rậm rạp. Tiếng quạ kêu rợn người...",
    "🌊 Ải 2: Dòng sông siết chắn ngang. Phải tìm đá tảng để nhảy qua!",
    "🌳 Ải 3: Cây cổ thụ Ngàn Năm đổ gãy chặn kín lối đi.",
    "🐺 Ải 4: Lục đục trong bụi rậm... Bầy sói hoang đang rình rập!",
    "🌿 Ải 5: Khí độc sương mù từ Đầm Lầy Hắc Ám dâng lên.",
    "🪨 Ải 6: Một vách núi dựng đứng, trơn trượt không điểm tựa.",
    "🌾 Ải 7: Đồng cỏ Gian Trá - Một bước sai là rơi xuống bẫy.",
    "🌲 Ải 8: Rừng Trúc Mê Cung - Bóng tối bao trùm, phương hướng đảo lộn.",
    "🏞️ Ải 9: Hồ Thủy Quái - Mặt nước tĩnh lặng đến đáng sợ...",
    "🐰 Ải 10: Ánh sáng le lói! Hang thỏ ngay phía trước nhưng Cửa Hang đã bị yểm bùa!"
]

# ====================== SESSION STATE ======================
def init_state():
    defaults = {
        "page": "intro", "name": "", "score": 0, "current_q": 0, 
        "time_left": 20, "answered": False, "is_dead": False
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

def next_level():
    st.session_state.current_q += 1
    st.session_state.time_left = 20
    st.session_state.answered = False
    safe_rerun()

def game_over():
    st.session_state.is_dead = True
    st.session_state.page = "result"
    safe_rerun()

# ====================== TRANG GIỚI THIỆU ======================
if st.session_state.page == "intro":
    st.markdown("<div class='rpg-header'><h1>⚔️ USAGI: SINH TỒN NƠI RỪNG SÂU ⚔️</h1></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background:rgba(0,0,0,0.7); padding:20px; border:2px solid #d4af37; border-radius:10px; margin-bottom: 20px; text-align:center;'>
        <h3 style='color:#ffea00;'>📜 GIAO ƯỚC KHẮC NGHIỆT 📜</h3>
        <p style='font-size:18px; line-height: 1.6;'>
        Thỏ Usagi đang đứng trước khu rừng Sinh Tử.<br>
        Có <strong>10 Ải Trận Pháp Toán Học</strong> chặn đường về hang.<br>
        <strong>Luật sinh tồn:</strong> Bạn có 20 giây cho mỗi ải. <br>
        Trượt dù chỉ 1 câu, Usagi sẽ vĩnh viễn kẹt lại trong rừng sâu.<br>
        Chỉ những kẻ đạt <strong>10/10</strong> mới xứng đáng sống sót!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    name = st.text_input("Tên Cứu Tinh (Người chơi):", placeholder="Nhập tên để ký giao ước...")
    
    if st.button("🔥 TIẾN VÀO RỪNG SÂU"):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.page = "game"
            safe_rerun()
        else:
            st.warning("⚠️ Vô danh tiểu tốt không thể vào rừng. Hãy xưng danh!")

# ====================== TRANG CHƠI CHÍNH ======================
elif st.session_state.page == "game":
    # Bảo vệ trường hợp lỗi logic index
    if st.session_state.current_q >= len(questions):
        st.session_state.page = "result"
        safe_rerun()

    q_idx = st.session_state.current_q
    q = questions[q_idx]
    
    # Header HUD
    col_hud1, col_hud2, col_hud3 = st.columns([1, 2, 1])
    with col_hud1:
        st.markdown(f"<div style='font-size:20px; color:#d4af37;'>👤 {st.session_state.name}</div>", unsafe_allow_html=True)
    with col_hud2:
        # Fix lỗi st.progress không hỗ trợ tham số text ở bản Streamlit cũ
        st.markdown(f"<div style='text-align:center; color:#a5d6a7; margin-bottom:5px;'>📍 Tiến trình: Ải {q_idx + 1}/10</div>", unsafe_allow_html=True)
        st.progress((q_idx) / 10)
    with col_hud3:
        st.markdown(f"<div style='text-align:right; font-size:20px; color:#ff4444;'>❤️ HP: 1/1</div>", unsafe_allow_html=True)

    # Khung Hoàn cảnh
    st.markdown(f"<div class='scene-text'>{scenes[q_idx]}</div>", unsafe_allow_html=True)
    
    # Cuộn giấy câu hỏi
    st.markdown(f"<div class='quest-box'>Ải {q_idx + 1}:<br><br>{q['q']}</div>", unsafe_allow_html=True)
    
    timer_placeholder = st.empty()
    
    # Xử lý Hết giờ tự động thua
    if not st.session_state.answered and st.session_state.time_left <= 0:
        st.session_state.answered = True
        timer_placeholder.markdown("<div class='timer-danger'>0</div>", unsafe_allow_html=True)
        st.markdown("<div class='feedback-wrong'>☠️ HẾT GIỜ! MỘT BƯỚC SẢY CHÂN...</div>", unsafe_allow_html=True)
        time.sleep(2)
        game_over()
        
    elif not st.session_state.answered:
        timer_placeholder.markdown(f"<div class='timer-danger'>{st.session_state.time_left}</div>", unsafe_allow_html=True)

    # Hiển thị đáp án
    cols = st.columns(2)
    for i, opt in enumerate(q["options"]):
        with cols[i % 2]:
            if st.button(opt, key=f"btn_{q_idx}_{i}", disabled=st.session_state.answered):
                st.session_state.answered = True
                
                if i == q["answer"]:
                    st.session_state.score += 1
                    st.markdown("<div class='feedback-correct'>✨ CHÍNH XÁC! PHÁ GIẢI THÀNH CÔNG! ✨</div>", unsafe_allow_html=True)
                    time.sleep(1.5)
                    if st.session_state.current_q < len(questions) - 1:
                        next_level()
                    else:
                        st.session_state.page = "result"
                        safe_rerun()
                else:
                    st.markdown("<div class='feedback-wrong'>☠️ SAI RỒI! TRÚNG BẪY CỦA RỪNG SÂU!</div>", unsafe_allow_html=True)
                    time.sleep(2)
                    game_over()

    # Vòng lặp đếm ngược timer (An toàn hơn)
    if not st.session_state.answered and st.session_state.time_left > 0:
        time.sleep(1)
        st.session_state.time_left -= 1
        safe_rerun()

# ====================== KẾT QUẢ ======================
elif st.session_state.page == "result":
    if not st.session_state.is_dead and st.session_state.score == 10:
        st.markdown("<div class='rpg-header'><h1 style='color:#00ffcc;'>👑 HÀNH TRÌNH HUYỀN THOẠI 👑</h1></div>", unsafe_allow_html=True)
        st.balloons()
        st.markdown(f"""
        <div style='background:rgba(0,50,0,0.8); padding:30px; text-align:center; border:3px solid #00ffcc; border-radius:15px; box-shadow: 0 0 30px #00ffcc;'>
            <h2 style='color:#ffffff;'>Chúc mừng Cứu Tinh {st.session_state.name}!</h2>
            <p style='font-size:22px; color:#a5d6a7;'>Bạn đã phá giải toàn bộ 10 Ải Sinh Tử.<br>Thỏ Usagi đã an toàn nằm trong chiếc hang ấm áp của mình.</p>
            <h1 style='font-size:60px;'>🏆</h1>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<div class='rpg-header'><h1 style='color:#ff3333;'>☠️ GAME OVER ☠️</h1></div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='background:rgba(50,0,0,0.8); padding:30px; text-align:center; border:3px solid #ff3333; border-radius:15px; box-shadow: 0 0 30px #ff0000;'>
            <h2 style='color:#ffffff;'>Bi kịch ập đến với {st.session_state.name}...</h2>
            <p style='font-size:22px; color:#ff9999;'>Thỏ Usagi đã gục ngã tại Ải thứ {st.session_state.current_q + 1}.<br>Rừng sâu lại có thêm một kẻ lạc lối vĩnh viễn.</p>
            <h1 style='font-size:60px;'>🪦</h1>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("---")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🔄 CHƠI LẠI TỪ ĐẦU", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            safe_rerun()
