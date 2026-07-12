import tkinter as tk
from tkinter import messagebox
import webbrowser

class MathQuizGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Toán Học Tư Duy - Thỏ Usagi")
        
        self.is_fullscreen = True
        self.root.attributes('-fullscreen', True)
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.exit_fullscreen)
        
        self.player_name = ""
        self.score = 0
        self.current_question = 0
        self.usagi_pos = [150, 550]
        self.timer_id = None
        self.timer_running = False

        self.questions = [
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
        
        self.show_name_input()

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes('-fullscreen', self.is_fullscreen)

    def exit_fullscreen(self, event=None):
        self.is_fullscreen = False
        self.root.attributes('-fullscreen', False)

    def cancel_timer(self):
        if self.timer_id is not None:
            try:
                self.root.after_cancel(self.timer_id)
            except:
                pass
            self.timer_id = None
        self.timer_running = False

    def show_name_input(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="🐰 TOÁN HỌC TƯ DUY", font=("Arial", 48, "bold"), 
                bg="#87CEEB", fg="#FF1493").pack(pady=120)
        tk.Label(self.root, text="Nhập tên của bạn:", font=("Arial", 24), bg="#87CEEB").pack(pady=20)
        
        self.name_entry = tk.Entry(self.root, font=("Arial", 22), width=30, justify='center')
        self.name_entry.pack(pady=15)
        self.name_entry.focus()
        
        tk.Button(self.root, text="BẮT ĐẦU CHƠI", font=("Arial", 20, "bold"), bg="#FF69B4", fg="white", height=2,
                 command=self.start_game).pack(pady=40)

    def start_game(self):
        self.player_name = self.name_entry.get().strip() or "Học Sinh"
        self.score = 0
        self.current_question = 0
        self.play_question()

    def play_question(self):
        self.cancel_timer()
        
        if self.current_question >= len(self.questions):
            self.show_result()
            return

        q = self.questions[self.current_question]
        
        for widget in self.root.winfo_children():
            widget.destroy()

        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        self.canvas = tk.Canvas(self.root, width=screen_w, height=screen_h, bg="#87CEEB", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_rectangle(0, 0, screen_w, screen_h//2 + 100, fill="#87CEEB")
        self.canvas.create_rectangle(0, screen_h//2 + 100, screen_w, screen_h, fill="#4682B4")
        self.canvas.create_oval(screen_w - 250, 80, screen_w - 120, 210, fill="#FFD700")

        self.canvas.create_text(screen_w//2, 60, text=f"Câu {self.current_question + 1}/10 • {self.player_name}", 
                              font=("Arial", 20, "bold"), fill="darkblue")
        self.canvas.create_text(screen_w - 200, 50, text=f"Điểm: {self.score}", font=("Arial", 22, "bold"), fill="#FF1493")

        self.canvas.create_text(screen_w//2, 160, text=q["q"], font=("Arial", 19, "bold"), 
                              width=screen_w - 120, fill="black")

        self.option_buttons = []
        self.option_positions = []
        
        for i, option in enumerate(q["options"]):
            y = 280 + i * 95
            btn = tk.Button(self.root, text=option, font=("Arial", 16), width=70, height=2,
                          bg="white", fg="black", relief="raised", bd=4,
                          command=lambda idx=i: self.select_answer(idx))
            btn.place(x=screen_w//2 - 380, y=y)
            self.option_buttons.append(btn)
            self.option_positions.append((screen_w//2 - 300, y + 35))

        self.usagi = self.canvas.create_text(self.usagi_pos[0], self.usagi_pos[1], 
                                           text="🐰", font=("Arial", 70), fill="#FF69B4")

        self.time_left = 15
        self.timer_label = self.canvas.create_text(180, 50, text=f"⏰ {self.time_left}s", 
                                                 font=("Arial", 24, "bold"), fill="red")
        
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if not self.timer_running:
            return
        if self.time_left > 0:
            self.canvas.itemconfig(self.timer_label, text=f"⏰ {self.time_left}s")
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.time_up()

    def animate_usagi(self, target_x, target_y):
        steps = 25
        dx = (target_x - self.usagi_pos[0]) / steps
        dy = (target_y - self.usagi_pos[1]) / steps
        
        def move_step(step):
            if step < steps:
                self.usagi_pos[0] += dx
                self.usagi_pos[1] += dy
                self.canvas.moveto(self.usagi, self.usagi_pos[0], self.usagi_pos[1])
                self.root.after(12, move_step, step + 1)
            else:
                self.canvas.itemconfig(self.usagi, text="🐇")
                self.root.after(400, lambda: self.canvas.itemconfig(self.usagi, text="🐰"))
        
        move_step(0)

    def select_answer(self, selected):
        self.cancel_timer()
        correct = self.questions[self.current_question]["answer"]
        target_x, target_y = self.option_positions[selected]
        self.animate_usagi(target_x - 100, target_y - 40)
        self.root.after(900, lambda: self.show_feedback(selected, correct))

    def show_feedback(self, selected, correct):
        if selected == correct:
            self.score += 1
            messagebox.showinfo("🎉 Đúng rồi!", "Usagi nhảy mừng!")
        else:
            messagebox.showerror("😢 Sai rồi!", 
                f"Đáp án đúng là:\n{self.questions[self.current_question]['options'][correct]}")
        self.current_question += 1
        self.play_question()

    def time_up(self):
        self.cancel_timer()
        messagebox.showinfo("⏰ Hết giờ!", "Thời gian đã hết cho câu này!")
        self.current_question += 1
        self.play_question()

    def show_result(self):
        self.cancel_timer()
        for widget in self.root.winfo_children():
            widget.destroy()
        
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        result_canvas = tk.Canvas(self.root, width=screen_w, height=screen_h, bg="#87CEEB")
        result_canvas.pack()

        result_canvas.create_text(screen_w//2, screen_h//2 - 120, text="KẾT THÚC!", 
                                font=("Arial", 60, "bold"), fill="#FF1493")
        result_canvas.create_text(screen_w//2, screen_h//2 - 40, text=f"{self.player_name}", 
                                font=("Arial", 32), fill="black")
        result_canvas.create_text(screen_w//2, screen_h//2 + 30, text=f"Điểm: {self.score}/10", 
                                font=("Arial", 40, "bold"), fill="green")
        
        percent = int(self.score / 10 * 100)
        result_canvas.create_text(screen_w//2, screen_h//2 + 120, text=f"{percent}%", 
                                font=("Arial", 70, "bold"), fill="#FF8C00")
        
        msg = "🎉 Xuất sắc! Usagi tự hào về bạn!" if percent >= 80 else "👍 Rất tốt!" if percent >= 60 else "💪 Cố gắng lần sau nhé!"
        result_canvas.create_text(screen_w//2, screen_h//2 + 200, text=msg, font=("Arial", 28), fill="#FF1493")

        # Nút Chơi lại
        tk.Button(self.root, text="Chơi Lại", font=("Arial", 18, "bold"), bg="#FF69B4", fg="white", height=2,
                 command=self.restart_game).place(x=screen_w//2 - 320, y=screen_h - 140, width=280)

        # Nút Đánh giá Game
        tk.Button(self.root, text="📋 Đánh giá Game", font=("Arial", 18, "bold"), bg="#00BFFF", fg="white", height=2,
                 command=self.open_feedback_form).place(x=screen_w//2 + 20, y=screen_h - 140, width=280)

        # Nút Thoát
        tk.Button(self.root, text="Thoát", font=("Arial", 18, "bold"), bg="gray", fg="white", height=2,
                 command=self.root.quit).place(x=screen_w//2 + 340, y=screen_h - 140, width=200)

    def open_feedback_form(self):
        webbrowser.open("https://forms.gle/JuZChBEuK8Q43aGj7")
        messagebox.showinfo("Cảm ơn!", "Đang mở form đánh giá.\nCảm ơn bạn đã góp ý nhé! 🐰")

    def restart_game(self):
        self.cancel_timer()
        self.show_name_input()

if __name__ == "__main__":
    game = MathQuizGame()
    game.root.mainloop()
