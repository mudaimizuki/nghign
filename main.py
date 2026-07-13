import streamlit as st
import time

st.set_page_config(page_title="Toán Học Tư Duy - Thỏ Usagi", layout="centered", page_icon="🐰")

# CSS
st.markdown("""
<style>
    .main {background: linear-gradient(180deg, #87CEEB 0%, #E0F7FA 50%, #90EE90 100%);}
    .stButton>button {
        background: linear-gradient(45deg, #00BFFF, #1E90FF);
        color: white; 
        font-size: 18px; 
        height: 65px; 
        width: 100%;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {transform: scale(1.05);}
    .correct {color: #00C853; font-size: 24px; font-weight: bold;}
    .wrong {color: #FF1744; font-size: 24px; font-weight: bold;}
    .question-box {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border: 3px solid #00BFFF;
    }
    .timer {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: #FF5722;
    }
</style>
""", unsafe_allow_html=True)

# Session state
if "page" not in st.session_state:
    st.session_state.page = "name"
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

def next_question():
    st.session_state.current_q += 1
    st.session_state.time_left = 20
    st.session_state.answered = False
    st.rerun()

# ==================== TRANG NHẬP TÊN ====================
if st.session_state.page == "name":
    st.title("🐰 **TOÁN HỌC TƯ DUY - THỎ USAGI**")
    st.markdown("<h3 style='text-align: center; color: #1E90FF;'>Hành trình trở về hang thỏ</h3>", unsafe_allow_html=True)
    name = st.text_input("Nhập tên của bạn:", placeholder="Ví dụ: Nguyễn Văn A")
    if st.button("🚀 BẮT ĐẦU HÀNH TRÌNH", type="primary", use_container_width=True):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.page = "game"
            st.rerun()
        else:
            st.warning("🐰 Usagi đang chờ tên của bạn!")

# ==================== TRANG CHƠI ====================
elif st.session_state.page == "game":
    q = questions[st.session_state.current_q]
    total = len(questions)

    st.markdown(f"<h2 style='text-align:center;'>🐰 Câu {st.session_state.current_q + 1} / {total}</h2>", unsafe_allow_html=True)
    
    # Progress
    progress = (st.session_state.current_q / total) * 100
    st.progress(progress)
    st.caption("🏞️ Tiến độ về hang")

    st.metric("🌟 Điểm số", st.session_state.score)

    # Câu hỏi
    st.markdown(f"<div class='question-box'><strong>{q['q']}</strong></div>", unsafe_allow_html=True)

    # Timer
    timer_placeholder = st.empty()
    if not st.session_state.answered:
        if st.session_state.time_left > 0:
            timer_placeholder.markdown(f"<div class='timer'>⏰ {st.session_state.time_left} giây</div>", unsafe_allow_html=True)
        else:
            st.session_state.answered = True
            st.error("⏰ Hết thời gian!")
            st.info(f"**Đáp án đúng:** {q['options'][q['answer']]}")
            time.sleep(2)
            if st.session_state.current_q < total - 1:
                next_question()
            else:
                st.session_state.page = "result"
                st.rerun()

    # === CÁC ĐÁP ÁN - ĐÃ FIX ===
    st.write("**Chọn đáp án đúng để giúp Usagi vượt chướng ngại vật:**")
    cols = st.columns(2)
    for i, opt in enumerate(q["options"]):
        with cols[i % 2]:
            if st.button(opt, key=f"btn_{st.session_state.current_q}_{i}", use_container_width=True):
                st.session_state.answered = True
                correct = q["answer"]
                
                if i == correct:
                    st.session_state.score += 1
                    st.success("🎉 **ĐÚNG RỒI!** Usagi nhảy mừng qua chướng ngại vật 🐰✨")
                else:
                    st.error("😢 **SAI RỒI!**")
                    st.info(f"**Đáp án đúng là:** {q['options'][correct]}")
                
                time.sleep(1.8)
                if st.session_state.current_q < total - 1:
                    next_question()
                else:
                    st.session_state.page = "result"
                    st.rerun()

    # Giảm thời gian (chạy sau khi render button)
    if not st.session_state.answered and st.session_state.time_left > 0:
        time.sleep(1)
        st.session_state.time_left -= 1
        st.rerun()

# ==================== KẾT QUẢ ====================
elif st.session_state.page == "result":
    st.title("🏆 **USAGI ĐÃ VỀ ĐẾN HANG!**")
    st.subheader(f"Chúc mừng {st.session_state.name}!")
    
    percent = int(st.session_state.score / len(questions) * 100)
    st.markdown(f"<h1 style='text-align: center; color: #00BFFF;'>{st.session_state.score}/{len(questions)} ({percent}%)</h1>", unsafe_allow_html=True)
    
    if percent >= 80:
        st.success("🎉 Xuất sắc! Usagi tự hào về bạn!")
        st.balloons()
    elif percent >= 60:
        st.info("👍 Rất tốt!")
    else:
        st.warning("💪 Cố gắng lần sau nhé!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🐰 Chơi Lại", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("📋 Đánh giá Game", type="secondary", use_container_width=True):
            st.markdown("[**Mở Form Đánh Giá**](https://forms.gle/JuZChBEuK8Q43aGj7)", unsafe_allow_html=True)
