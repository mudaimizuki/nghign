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

        self.questions = [ ... ]  # Giữ nguyên 10 câu hỏi như trước

        self.show_name_input()

    # (Các hàm toggle_fullscreen, exit_fullscreen, cancel_timer giữ nguyên như code cũ)

    def show_name_input(self):
        # ... (giữ nguyên)

    def start_game(self):
        # ... (giữ nguyên)

    def play_question(self):
        # ... (giữ nguyên)

    def update_timer(self):
        # ... (giữ nguyên)

    def animate_usagi(self, target_x, target_y):
        # ... (giữ nguyên)

    def select_answer(self, selected):
        # ... (giữ nguyên)

    def show_feedback(self, selected, correct):
        # ... (giữ nguyên)

    def time_up(self):
        # ... (giữ nguyên)

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

        # Nút Đánh giá Game (mới)
        tk.Button(self.root, text="📋 Đánh giá Game", font=("Arial", 18, "bold"), bg="#00BFFF", fg="white", height=2,
                 command=self.open_feedback_form).place(x=screen_w//2 + 20, y=screen_h - 140, width=280)

        # Nút Thoát
        tk.Button(self.root, text="Thoát", font=("Arial", 18, "bold"), bg="gray", fg="white", height=2,
                 command=self.root.quit).place(x=screen_w//2 + 340, y=screen_h - 140, width=200)

    def open_feedback_form(self):
        webbrowser.open("https://forms.gle/JuZChBEuK8Q43aGj7")
        messagebox.showinfo("Cảm ơn!", "Đang mở form đánh giá. Cảm ơn bạn đã góp ý nhé! 🐰")

    def restart_game(self):
        self.cancel_timer()
        self.show_name_input()

    # (Các hàm còn lại giữ nguyên như code trước)

if __name__ == "__main__":
    game = MathQuizGame()
    game.root.mainloop()
