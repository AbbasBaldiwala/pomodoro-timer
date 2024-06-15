from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMG_HEIGHT = 234
IMG_WIDTH = 200
CHECK_MARK = "✔"
reps = 0
timer = None
want_pause = True

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        countdown(long_break_sec)
        reps = 0
        check_marks.config(text="")
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(sec):
    global reps
    global timer
    count_min = math.floor(sec/60)
    count_sec = sec % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if sec > 0:
        timer = window.after(1000, countdown, sec - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(IMG_WIDTH / 2, IMG_HEIGHT / 2, image=tomato_img)
timer_text = canvas.create_text(IMG_WIDTH / 2, IMG_HEIGHT - 100, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 14, "normal"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
