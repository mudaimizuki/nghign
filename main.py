import streamlit as st
import time
import random

st.set_page_config(page_title="Thỏ Usagi - Hành Trình Về Hang", layout="centered", page_icon="🐰")

# ====================== CSS ĐỈNH CAO - RỪNG RỪNG SÔNG HỒ ======================
st.markdown("""
<style>
    .main {
        background: linear-gradient(180deg, #0f2b1a 0%, #1e3f2b 40%, #2e5c3d 70%, #4a8c5f 100%);
        color: #e0f2e9;
    }
    .header {
        text-align: center;
        padding: 20px;
        background: rgba(0,0,0,0.4);
        border-radius: 20px;
        margin-bottom: 20px;
        border: 4px solid #ffd700;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff8c00, #ffd700);
        color: #1a3c2e;
        font-size: 18px;
        font-weight: bold;
        height: 70px;
        width: 100%;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.4);
        border: 3px solid #1a3c2e;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.08) rotate(2deg);
        box-shadow: 0 10px 20px rgba(255, 215, 0, 0.5);
    }
    .question-box {
        background: linear-gradient(135deg, #ffffff, #f0f8f0);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 5px solid #228b22;
        color: #1a3c2e;
        font-size: 18px;
        margin: 20px 0;
    }
    .timer {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #ff4500;
        text-shadow: 0 0 10px #ff0000;
        padding: 10px;
        border: 4px solid #ff4500;
        border-radius: 15px;
        background: rgba(0,0,0,0.7);
    }
    .scene {
        font-size: 20px;
        text-align: center;
        padding: 15px;
        background: rgba(34, 139, 34, 0.3);
        border-radius: 15px;
        margin: 15px 0;
        border-left: 6px solid #ffd700;
    }
    .progress-container {
        background: rgba(0,0,0,0.4);
        padding: 15px;
        border-radius: 15px;
        margin: 15px 0;
    }
    .correct {color: #00ff7f; font-size: 28px; font-weight: bold; text-shadow: 0 0 10px #00ff00;}
    .wrong {color: #ff1744; font-size: 28px; font-weight: bold; text-shadow: 0 0 10px #ff0000;}
    .path {
        text-align: center;
        font-size: 28px;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "page" not in st.session_state:
    st.session_state.page = "intro"
if "name" not in st.session_state:
    st.session_state.name = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "time_left" not in st.session_state:
    st.session_state.time_left = 20
if "answered" not in st.session_state:
    st.session_state.answered = False
if "path_progress" not in st.session_state:
    st.session_state.path_progress = 0

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
    "🌲 Usagi đang băng qua khu rừng rậm rạp đầu tiên...",
    "🌊 Một con sông lớn chắn ngang đường, Usagi cần nhảy qua!",
    "🌳 Cây cổ thụ khổng lồ đổ chắn lối, phải vượt qua!",
    "🐺 Bầy sói hoang xuất hiện, Usagi cần nhanh trí!",
    "🌿 Đầm lầy sương mù bao phủ, tìm đường thoát!",
    "🪨 Núi đá cheo leo hiện ra trước mặt...",
    "🌾 Đồng cỏ hoang vu đầy chướng ngại...",
    "🌲 Rừng tre trúc tối om, Usagi lạc lối...",
    "🏞️ Hồ nước trong xanh nhưng đầy nguy hiểm...",
    "🐰 Hang thỏ quen thuộc đã hiện ra ở cuối đường!"
]

def next_question():
    st.session_state.current_q += 1
    st.session_state.time_left = 20
    st.session_state.answered = False
    st.session_state.path_progress = min(100, (st.session_state.current_q / len(questions)) * 100)
    st.rerun()

# ====================== TRANG GIỚI THIỆU ======================
if st.session_state.page == "intro":
    st.markdown("<div class='header'><h1>🐰 <strong>THỎ USAGI - HÀNH TRÌNH VỀ HANG</strong> 🏠</h1></div>", unsafe_allow_html=True)
    
    st.image("https://picsum.photos/id/1015/800/400", use_column_width=True)  # Forest image placeholder
    
    st.markdown("""
    <div style='text-align:center; font-size:22px; padding:20px; background:rgba(0,0,0,0.4); border-radius:15px;'>
        <strong>🌲 Chào mừng đến với khu rừng huyền bí!</strong><br><br>
        Thỏ Usagi lạc đường và đang cố gắng trở về hang thỏ. <br>
        Trên đường có <strong>10 chướng ngại vật</strong> đầy thử thách toán học.<br>
        Giúp Usagi trả lời đúng tất cả để về hang an toàn nhé!
    </div>
    """, unsafe_allow_html=True)
    
    name = st.text_input("🐰 Nhập tên nhà thám hiểm của bạn:", placeholder="Ví dụ: Lan Anh, Minh Quân...")
    
    if st.button("🚀 BẮT ĐẦU HÀNH TRÌNH VỀ HANG", type="primary", use_container_width=True):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.page = "game"
            st.rerun()
        else:
            st.warning("🐰 Usagi đang chờ tên của bạn!")

# ====================== TRANG CHƠI CHÍNH ======================
elif st.session_state.page == "game":
    q_idx = st.session_state.current_q
    q = questions[q_idx]
    total = len(questions)
    
    # Header
    st.markdown(f"<div class='header'><h2>🌲 HÀNH TRÌNH CỦA {st.session_state.name.upper()} 🐰</h2></div>", unsafe_allow_html=True)
    
    # Progress path
    st.markdown(f"""
    <div class='path'>
        Tiến độ về hang: <strong>{q_idx + 1} / {total}</strong> chướng ngại vật<br>
        <span style='font-size:18px;'>{'🪨' * (q_idx + 1)}{'🌲' * (total - q_idx - 1)}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.progress(st.session_state.path_progress / 100)
    
    # Current scene
    st.markdown(f"<div class='scene'>{scenes[q_idx]}</div>", unsafe_allow_html=True)
    
    st.metric("🌟 Số chướng ngại đã vượt", f"{st.session_state.score} / {q_idx}")
    
    # Question
    st.markdown(f"<div class='question-box'><strong>Câu {q_idx + 1}: {q['q']}</strong></div>", unsafe_allow_html=True)
    
    # Timer
    timer_placeholder = st.empty()
    
    if not st.session_state.answered:
        if st.session_state.time_left > 0:
            timer_placeholder.markdown(f"<div class='timer'>⏰ {st.session_state.time_left} GIÂY</div>", unsafe_allow_html=True)
        else:
            st.session_state.answered = True
            st.error("⏰ HẾT THỜI GIAN! Usagi bị kẹt lại...")
            st.info(f"**Đáp án đúng:** {q['options'][q['answer']]}")
            time.sleep(2.5)
            if st.session_state.current_q < total - 1:
                next_question()
            else:
                st.session_state.page = "result"
                st.rerun()
    
    # Options
    st.write("**Chọn đáp án đúng để giúp Usagi vượt chướng ngại:**")
    cols = st.columns(2)
    for i, opt in enumerate(q["options"]):
        with cols[i % 2]:
            if st.button(opt, key=f"btn_{q_idx}_{i}", use_container_width=True):
                st.session_state.answered = True
                correct = q["answer"]
                
                if i == correct:
                    st.session_state.score += 1
                    st.markdown("<p class='correct'>🎉 ĐÚNG RỒI! Usagi đã vượt qua chướng ngại vật! 🐰✨</p>", unsafe_allow_html=True)
                else:
                    st.markdown("<p class='wrong'>😢 SAI RỒI! Usagi gặp khó khăn...</p>", unsafe_allow_html=True)
                    st.info(f"**Đáp án đúng:** {q['options'][correct]}")
                
                time.sleep(2)
                if st.session_state.current_q < total - 1:
                    next_question()
                else:
                    st.session_state.page = "result"
                    st.rerun()
    
    # Timer countdown
    if not st.session_state.answered and st.session_state.time_left > 0:
        time.sleep(1)
        st.session_state.time_left -= 1
        st.rerun()

# ====================== KẾT QUẢ ======================
elif st.session_state.page == "result":
    st.markdown("<div class='header'><h1>🏆 KẾT THÚC HÀNH TRÌNH 🏠</h1></div>", unsafe_allow_html=True)
    
    percent = int(st.session_state.score / len(questions) * 100)
    
    if st.session_state.score == len(questions):
        st.success("🎉 **CHÚC MỪNG!** Thỏ Usagi đã về đến hang an toàn!")
        st.balloons()
        st.image("https://picsum.photos/id/1016/800/400", use_column_width=True)
        st.markdown(f"""
        <h2 style='text-align:center; color:#ffd700;'>
            {st.session_state.name} đã dẫn dắt Usagi vượt qua tất cả 10 chướng ngại vật!<br>
            Bạn là nhà thám hiểm xuất sắc nhất khu rừng!
        </h2>
        """, unsafe_allow_html=True)
    else:
        st.warning("🐰 Usagi chưa về được hang hoàn toàn...")
        st.markdown(f"""
        <h3 style='text-align:center;'>
            {st.session_state.name} đã giúp Usagi vượt qua <strong>{st.session_state.score}</strong>/{len(questions)} chướng ngại vật ({percent}%)
        </h3>
        """, unsafe_allow_html=True)
        if percent >= 70:
            st.info("🌟 Rất gần rồi! Usagi tự hào về bạn.")
        else:
            st.info("💪 Cố gắng lần sau để đưa Usagi về hang nhé!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌲 Chơi Lại Hành Trình", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("📋 Đánh giá Hành Trình", type="secondary", use_container_width=True):
            st.markdown("[**Mở Form Đánh Giá**](https://forms.gle/JuZChBEuK8Q43aGj7)", unsafe_allow_html=True)
