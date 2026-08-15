import tkinter as tk

# --- KONFIGURASI TIMER ---
# Ubah TEST_MODE = False jika ingin waktu Pomodoro nyata (25m / 5m / 15m)
TEST_MODE = True

if TEST_MODE:
    WORK_TIME = 10        # 10 detik (Testing Cepat)
    SHORT_BREAK = 5       # 5 detik
    LONG_BREAK = 15       # 15 detik
else:
    WORK_TIME = 25 * 60   # 25 menit
    SHORT_BREAK = 5 * 60  # 5 menit
    LONG_BREAK = 15 * 60  # 15 menit

# Inisialisasi variabel state
session_count = 0
timer_running = False
timer_after_id = None

def countdown(seconds):
    global timer_running, timer_after_id
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        # Update setiap 1 detik
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
            # Sesi Long Break (setiap kelipatan 8)
            desc = "15 detik" if TEST_MODE else "15 menit"
            status_label.config(text=f"🎉 Long Break ({desc})", fg="red")
            countdown(LONG_BREAK)
        elif session_count % 2 == 1:
            # Sesi Kerja (Work Session 1, 3, 5, 7)
            work_num = (session_count + 1) // 2
            desc = "10 detik" if TEST_MODE else "25 menit"
            status_label.config(text=f"💻 Work Session #{work_num} ({desc})", fg="green")
            countdown(WORK_TIME)
        else:
            # Sesi Istirahat Pendek (Short Break 2, 4, 6)
            desc = "5 detik" if TEST_MODE else "5 menit"
            status_label.config(text=f"☕ Short Break ({desc})", fg="orange")
            countdown(SHORT_BREAK)

def reset_timer():
    global timer_running, session_count, timer_after_id
    if timer_after_id is not None:
        window.after_cancel(timer_after_id)
        timer_after_id = None
    timer_running = False
    session_count = 0
    
    init_mins, init_secs = divmod(WORK_TIME, 60)
    timer_label.config(text=f"{init_mins:02d}:{init_secs:02d}")
    status_label.config(text="Work Session", fg="green")

# --- GUI Setup ---
window = tk.Tk()
window.title("Pomodoro Timer" + (" (⚡ Test Mode)" if TEST_MODE else ""))
window.geometry("380x260")
window.resizable(False, False)

# Label Status Sesi
status_label = tk.Label(window, text="Work Session", font=("Arial", 14, "bold"), fg="green")
status_label.pack(pady=15)

# Label Waktu Timer
init_mins, init_secs = divmod(WORK_TIME, 60)
timer_label = tk.Label(window, text=f"{init_mins:02d}:{init_secs:02d}", font=("Arial", 45, "bold"))
timer_label.pack(pady=10)

# Frame Tombol Kontrol
controls_frame = tk.Frame(window)
controls_frame.pack(pady=15)

start_button = tk.Button(controls_frame, text="Start", font=("Arial", 12, "bold"), width=8, bg="#4CAF50", fg="white", command=start_timer)
start_button.pack(side="left", padx=10)

reset_button = tk.Button(controls_frame, text="Reset", font=("Arial", 12, "bold"), width=8, bg="#f44336", fg="white", command=reset_timer)
reset_button.pack(side="left", padx=10)

if __name__ == "__main__":
    window.mainloop()
