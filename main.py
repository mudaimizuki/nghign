import streamlit as st
import time
import random

st.set_page_config(page_title="Toán Học Tư Duy - Thỏ Usagi", layout="centered")

# CSS làm đẹp
st.markdown("""
<style>
    .big-font { font-size: 32px !important; font-weight: bold; }
    .question { font-size: 22px !important; }
    .timer { font-size: 28px !important; color: red; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Dữ liệu câu hỏi
questions = [
    {"q": "Kí hiệu nào dưới đây dùng để viết tổ hợp chập 4 của 8 phần tử?", 
     "options": ["A. 70", "B. 20", "C. 216", "D. 150"], "answer": 0},
    {"q": "Khai triển biểu thức x²(3x-2)⁵ ta nhận được bao nhiêu số hạng?", 
     "options": ["A. C(8,4)", "B. C(4,8)", "C. A(8,4)", "D. A(4,8)"], "answer": 0},
    {"q": "Một hộp chứa 12 sản phẩm tốt và 4 sản phẩm kém chất lượng, rút ngẫu nhiên 3 sản phẩm. Số phần tử của không gian mẫu là?", 
     "options": ["A. 6", "B. 5", "C. 7", "D. 8"], "answer": 2},
    {"q": "Số cách chọn 2 học sinh từ 5 học sinh là", 
     "options": ["A. C(3,16)", "B. C(3,4)", "C. C(3,8)", "D. C(3,12)"], "answer": 1},
    {"q": "Số hạng không chứa x trong khai triển (√x - 3/x)³ là", 
     "options": ["A. 2⁵", "B. C(2,5)", "C. A(2,5)", "D. 5²"], "answer": 3},
    {"q": "Cho phép thử ngẫu nhiên. Phát biểu nào sau đây là đúng?", 
     "options": ["A. 3", "B. -9", "C. -3", "D. 9"], "answer": 1},
    {"q": "Trong không gian mẫu, biến cố chắc chắn là biến cố như thế nào?", 
     "options": ["A. Là biến cố có xác suất bằng 0.", "B. Là biến cố luôn xảy ra khi thực hiện phép thử.", "C. Là biến cố không bao giờ xảy ra.", "D. Là biến cố chỉ có một kết quả duy nhất."], "answer": 1},
    {"q": "Phương trình tổng quát của đường thẳng có dạng là:", 
     "options": ["A. ax² + by + c = 0.", "B. y = ax + b.", "C. ax + by + c = 0 (với a² + b² > 0).", "D. x = x₀ + at; y = y₀ + bt."], "answer": 2},
    {"q": "Phát biểu nào sau đây là đúng về hai đường thẳng song song trong mặt phẳng?", 
     "options": ["A. Hai đường thẳng song song là hai đường thẳng có vectơ pháp tuyến cùng phương.", "B. Hai đường thẳng song song là hai đường thẳng có vectơ chỉ phương vuông góc.", "C. Hai đường thẳng song song không bao giờ có cùng hệ số góc.", "D. Hai đường thẳng song song là hai đường thẳng cắt nhau tại một điểm."], "answer": 0},
    {"q": "Trong mặt phẳng Oxy, phương trình nào sau đây là phương trình chính tắc của một đường tròn?", 
     "options": ["A. x² + y² = -4", "B. x² + y² = 0", "C. x² - y² = 4", "D. x² + y² = 4"], "answer": 3}
]

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.name = ""
    st.session_state.answers = []

# Trang chính
st.title("🐰 Toán Học Tư Duy - Thỏ Usagi")

if st.session_state.name == "":
    st.subheader("Nhập tên của bạn")
    name = st.text_input("Tên:", placeholder="Ví dụ: Nguyễn Văn A")
    if st.button("Bắt Đầu Chơi", type="primary"):
        if name.strip():
            st.session_state.name = name.strip()
            st.rerun()
        else:
            st.warning("Vui lòng nhập tên!")
else:
    progress = st.progress(st.session_state.current_q / len(questions))
    st.write(f"**Người chơi:** {st.session_state.name} | **Điểm:** {st.session_state.score}/{st.session_state.current_q}")

    if st.session_state.current_q < len(questions):
        q = questions[st.session_state.current_q]
        
        st.subheader(f"Câu {st.session_state.current_q + 1}/10")
        st.markdown(f"<p class='question'>{q['q']}</p>", unsafe_allow_html=True)

        # Timer giả lập (Streamlit không có timer thật, nên dùng button)
        answer = st.radio("Chọn đáp án:", q["options"], key=f"q{st.session_state.current_q}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Nộp đáp án", type="primary"):
                selected_idx = q["options"].index(answer)
                correct_idx = q["answer"]
                
                if selected_idx == correct_idx:
                    st.session_state.score += 1
                    st.success("🎉 Đúng rồi! Usagi nhảy mừng!")
                else:
                    st.error(f"😢 Sai rồi! Đáp án đúng là: **{q['options'][correct_idx]}**")
                
                st.session_state.current_q += 1
                st.rerun()
    else:
        # Kết quả cuối cùng
        st.balloons()
        percent = int(st.session_state.score / len(questions) * 100)
        
        st.success(f"**Kết thúc!** Bạn được **{st.session_state.score}/{len(questions)}** điểm ({percent}%)")
        
        if percent >= 80:
            st.write("🎉 **Xuất sắc!** Usagi tự hào về bạn!")
        elif percent >= 60:
            st.write("👍 Rất tốt!")
        else:
            st.write("💪 Cố gắng lần sau nhé!")

        st.markdown("### 📋 Đánh giá Game")
        st.write("Bạn vui lòng dành 1 phút đánh giá game để mình cải thiện nhé!")
        
        if st.button("📝 Mở Form Đánh Giá", type="primary"):
            st.markdown("[**Nhấn vào đây để mở form khảo sát**](https://forms.gle/JuZChBEuK8Q43aGj7)", unsafe_allow_html=True)
        
        if st.button("Chơi Lại"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

st.caption("Game được làm bằng Streamlit • Usagi dễ thương 🐰")
