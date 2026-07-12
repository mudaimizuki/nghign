import streamlit as st
import time
import random

st.set_page_config(page_title="Toán Học Tư Duy - Thỏ Usagi", layout="centered")

# CSS tùy chỉnh - Giao diện xanh trắng
st.markdown("""
<style>
    .main {background: linear-gradient(#E0F7FA, #FFFFFF);}
    .stButton>button {background-color: #00BFFF; color: white; font-size: 18px; height: 60px; width: 100%;}
    .correct {color: #00C853; font-size: 22px;}
    .wrong {color: #FF1744; font-size: 22px;}
</style>
""", unsafe_allow_html=True)

# Khởi tạo session
if "page" not in st.session_state:
    st.session_state.page = "name"
if "name" not in st.session_state:
    st.session_state.name = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "time_left" not in st.session_state:
    st.session_state.time_left = 15

questions = [
    {"q": "Kí hiệu nào dưới đây dùng để viết tổ hợp chập 4 của 8 phần tử?", "options": ["A. 70", "B. 20", "C. 216", "D. 150"], "answer": 0},
    {"q": "Khai triển biểu thức x²(3x-2)⁵ ta nhận được bao nhiêu số hạng?", "options": ["A. C(8,4)", "B. C(4,8)", "C. A(8,4)", "D. A(4,8)"], "answer": 0},
    {"q": "Một hộp chứa 12 sản phẩm tốt và 4 sản phẩm kém chất lượng, rút ngẫu nhiên 3 sản phẩm. Số phần tử của không gian mẫu là?", "options": ["A. 6", "B. 5", "C. 7", "D. 8"], "answer": 2},
    {"q": "Số cách chọn 2 học sinh từ 5 học sinh là", "options": ["A. C(3,16)", "B. C(3,4)", "C. C(3,8)", "D. C(3,12)"], "answer": 1},
    {"q": "Số hạng không chứa x trong khai triển (√x - 3/x)³ là", "options": ["A. 2⁵", "B. C(2,5)", "C. A(2,5)", "D. 5²"], "answer": 3},
    {"q": "Cho phép thử ngẫu nhiên. Phát biểu nào sau đây là đúng?", "options": ["A. 3", "B. -9", "C. -3", "D. 9"], "answer": 1},
    {"q": "Trong không gian mẫu, biến cố chắc chắn là biến cố như thế nào?", "options": ["A. Là biến cố có xác suất bằng 0.", "B. Là biến cố luôn xảy ra khi thực hiện phép thử.", "C. Là biến cố không bao giờ xảy ra.", "D. Là biến cố chỉ có một kết quả duy nhất."], "answer": 1},
    {"q": "Phương trình tổng quát của đường thẳng có dạng là:", "options": ["A. ax² + by + c = 0.", "B. y = ax + b.", "C. ax + by + c = 0 (với a² + b² > 0).", "D. x = x₀ + at; y = y₀ + bt."], "answer": 2},
    {"q": "Phát biểu nào sau đây là đúng về hai đường thẳng song song trong mặt phẳng?", "options": ["A. Hai đường thẳng song song là hai đường thẳng có vectơ pháp tuyến cùng phương.", "B. Hai đường thẳng song song là hai đường thẳng có vectơ chỉ phương vuông góc.", "C. Hai đường thẳng song song không bao giờ có cùng hệ số góc.", "D. Hai đường thẳng song song là hai đường thẳng cắt nhau tại một điểm."], "answer": 0},
    {"q": "Trong mặt phẳng Oxy, phương trình nào sau đây là phương trình chính tắc của một đường tròn?", "options": ["A. x² + y² = -4", "B. x² + y² = 0", "C. x² - y² = 4", "D. x² + y² = 4"], "answer": 3}
]

def next_question():
    st.session_state.current_q += 1
    st.session_state.time_left = 15
    st.rerun()

# ==================== TRANG NHẬP TÊN ====================
if st.session_state.page == "name":
    st.title("🐰 TOÁN HỌC TƯ DUY")
    st.subheader("Chào mừng bạn!")
    name = st.text_input("Nhập tên của bạn:", placeholder="Ví dụ: Nguyễn Văn A")
    
    if st.button("BẮT ĐẦU CHƠI", type="primary", use_container_width=True):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.page = "game"
            st.rerun()
        else:
            st.warning("Vui lòng nhập tên!")

# ==================== TRANG CHƠI ====================
elif st.session_state.page == "game":
    q = questions[st.session_state.current_q]
    
    st.title(f"Câu {st.session_state.current_q + 1}/10")
    st.subheader(st.session_state.name)
    st.progress(st.session_state.score / len(questions))
    
    col1, col2 = st.columns([3,1])
    with col1:
        st.write(f"**{q['q']}**")
    with col2:
        st.metric("Điểm", st.session_state.score)
    
    # Timer
    if st.session_state.time_left > 0:
        timer_placeholder = st.empty()
        for t in range(st.session_state.time_left, 0, -1):
            timer_placeholder.markdown(f"<h2 style='color: #FF5722; text-align: center;'>⏰ {t} giây</h2>", unsafe_allow_html=True)
            time.sleep(1)
            st.session_state.time_left = t - 1
            if st.session_state.time_left == 0:
                st.rerun()
    
    st.write("Chọn đáp án:")
    for i, opt in enumerate(q["options"]):
        if st.button(opt, key=f"btn_{i}", use_container_width=True):
            correct = q["answer"]
            if i == correct:
                st.session_state.score += 1
                st.success("🎉 Đúng rồi! Usagi nhảy mừng!")
            else:
                st.error(f"😢 Sai rồi! Đáp án đúng là: **{q['options'][correct]}**")
            
            time.sleep(1.5)
            next_question()

    if st.session_state.current_q >= len(questions):
        st.session_state.page = "result"
        st.rerun()

# ==================== KẾT QUẢ + FORM ====================
elif st.session_state.page == "result":
    st.title("🏆 KẾT THÚC!")
    st.subheader(f"Chúc mừng {st.session_state.name}!")
    
    percent = int(st.session_state.score / len(questions) * 100)
    st.markdown(f"<h1 style='text-align: center; color: #00BFFF;'>{st.session_state.score}/{len(questions)} ({percent}%)</h1>", unsafe_allow_html=True)
    
    if percent >= 80:
        st.success("🎉 Xuất sắc! Usagi tự hào về bạn!")
    elif percent >= 60:
        st.info("👍 Rất tốt!")
    else:
        st.warning("💪 Cố gắng lần sau nhé!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Chơi Lại", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    with col2:
        if st.button("📋 Đánh giá Game", type="secondary", use_container_width=True):
            st.markdown("[**Mở Form Đánh Giá**](https://forms.gle/JuZChBEuK8Q43aGj7)", unsafe_allow_html=True)

    st.balloons()
