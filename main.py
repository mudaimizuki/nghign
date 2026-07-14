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
    
    # Dùng component mặc định của Streamlit để đảm bảo link chắc chắn hiển thị
    st.markdown("<h3 style='text-align: center; color: #ffea00;'>Khảo sát Hành Trình 👇</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Hộp thông báo chứa link khảo sát cực kỳ nổi bật
        st.info("📝 **[NHẤN VÀO ĐÂY ĐỂ GỬI THƯ MẬT (ĐÁNH GIÁ GAME)](https://forms.gle/JuZChBEuK8Q43aGj7)**")
        
        st.write("") # Tạo một chút khoảng trống
        
        # Nút Chơi Lại
        if st.button("🔄 CHƠI LẠI TỪ ĐẦU", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            safe_rerun()
