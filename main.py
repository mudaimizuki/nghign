import streamlit as st
import time
import random

st.set_page_config(page_title="Toán Học Tư Duy - Thỏ Usagi", layout="centered")

# CSS để đẹp hơn
st.markdown("""
<style>
    .big-font { font-size: 42px !important; font-weight: bold; color: #FF1493; }
    .question { font-size: 22px !important; }
    .timer { font-size: 28px !important; color: red; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Khởi tạo session
if 'page' not in st.session_state:
    st.session_state.page = "name"
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'time_left' not in st.session_state:
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

def reset_game():
    st.session_state.score = 0
    st.session_state.current_q = 0
    st.session_state.time_left = 15
    st.session_state.page = "name"

if st.session_state.page == "name":
    st.markdown("<h1 class='big-font'>🐰 TOÁN HỌC TƯ DUY</h1>", unsafe_allow_html=True)
    name = st.text_input("Nhập tên của bạn:", placeholder="Ví dụ: Nguyễn Văn A")
    if st.button("BẮT ĐẦU CHƠI", type="primary"):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.page = "game"
            st.rerun()
        else:
            st.warning("Vui lòng nhập tên!")

elif st.session_state.page == "game":
    q = questions[st.session_state.current_q]
    
    st.markdown(f"**Câu {st.session_state.current_q + 1}/10** - Chào **{st.session_state.name}**")
    st.markdown(f"**Điểm hiện tại:** {st.session_state.score}")
    
    # Timer
    timer_placeholder = st.empty()
    
    # Câu hỏi
    st.markdown(f"### {q['q']}")
    
    # Options
    selected = None
    for i, opt in enumerate(q["options"]):
        if st.button(opt, key=f"btn_{i}", use_container_width=True):
            selected = i
            break
    
    # Logic timer (Streamlit khó làm countdown realtime, nên dùng button "Trả lời")
    if selected is not None:
        if selected == q["answer"]:
            st.session_state.score += 1
            st.success("🎉 Đúng rồi! Usagi nhảy mừng!")
        else:
            st.error(f"😢 Sai rồi! Đáp án đúng là: {q['options'][q['answer']]}")
        
        if st.session_state.current_q < len(questions) - 1:
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.session_state.page = "result"
            st.rerun()

    # Nút hết giờ
    if st.button("⏰ Hết giờ (bỏ qua)"):
        st.warning("Thời gian đã hết!")
        if st.session_state.current_q < len(questions) - 1:
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.session_state.page = "result"
            st.rerun()

elif st.session_state.page == "result":
    st.balloons()
    st.markdown("<h1 class='big-font'>KẾT THÚC!</h1>", unsafe_allow_html=True)
    st.markdown(f"**{st.session_state.name}** đạt **{st.session_state.score}/10** điểm")
    
    percent = int(st.session_state.score / 10 * 100)
    st.markdown(f"### {percent}%")
    
    if percent >= 80:
        st.success("🎉 Xuất sắc! Usagi rất tự hào về bạn!")
    elif percent >= 60:
        st.info("👍 Bạn làm rất tốt!")
    else:
        st.warning("💪 Cố gắng lần sau nhé!")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Chơi Lại", type="primary"):
            reset_game()
            st.rerun()
    with col2:
        if st.button("📋 Đánh giá Game", type="secondary"):
            st.markdown("[🔗 Mở Form Đánh Giá](https://forms.gle/JuZChBEuK8Q43aGj7)")
            st.success("Cảm ơn bạn đã đánh giá!")

# Footer
st.caption("Made with ❤️ for learning")
