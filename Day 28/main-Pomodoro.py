import tkinter
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
reps = 0
# checks = ""
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    # count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global my_timer
    # global checks
    # print(count)
    # Format the count left in minutes and seconds 00:00
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # if reps % 2 == 0:
        #     checks += "✔"
        #     check_marks.config(text=checks)
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# count_down(5)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

# count_down(5)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.config(padx=5, pady=5)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.config(padx=5, pady=5)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text="", fg=GREEN, bg=YELLOW)
check_marks.config(padx=5, pady=5)
check_marks.grid(column=1, row=3)


window.mainloop()
