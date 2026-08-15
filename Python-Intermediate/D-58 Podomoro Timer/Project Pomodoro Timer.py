import tkinter as tk

session_count = 0
timer_running = False
timer_after_id = None

def countdown(seconds):
    global timer_running, timer_after_id
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        timer_after_id = window.after(1000, countdown, seconds - 1)
    else:
        timer_running = False
        start_timer()

def start_timer():
    global session_count, timer_running
    if not timer_running:
        timer_running = True
        session_count += 1

        if session_count % 8 == 0:
            status_label.config(text="Long Break (15 min)", fg="red")
            countdown(15 * 60)
        elif session_count % 2 == 1:
            work_num = (session_count + 1) // 2
            status_label.config(text=f"Work Session #{work_num} (25 min)", fg="green")
            countdown(25 * 60)
        else:
            status_label.config(text="Short Break (5 min)", fg="orange")
            countdown(5 * 60)

def reset_timer():
    global timer_running, session_count, timer_after_id
    if timer_after_id is not None:
        window.after_cancel(timer_after_id)
        timer_after_id = None
    timer_running = False
    session_count = 0
    timer_label.config(text="25:00")
    status_label.config(text="Work Session", fg="green")

# --- UI Setup ---
window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("350x250")
window.resizable(False, False)

status_label = tk.Label(window, text="Work Session", font=("Arial", 14, "bold"), fg="green")
status_label.pack(pady=15)

timer_label = tk.Label(window, text="25:00", font=("Arial", 45, "bold"))
timer_label.pack(pady=10)

controls_frame = tk.Frame(window)
controls_frame.pack(pady=15)

start_button = tk.Button(controls_frame, text="Start", font=("Arial", 12, "bold"), width=8, bg="#4CAF50", fg="white", command=start_timer)
start_button.pack(side="left", padx=10)

reset_button = tk.Button(controls_frame, text="Reset", font=("Arial", 12, "bold"), width=8, bg="#f44336", fg="white", command=reset_timer)
reset_button.pack(side="left", padx=10)

if __name__ == "__main__":
    window.mainloop()
