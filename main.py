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
rep = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer", fg=GREEN)
    label_2.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if rep is 1/3/5/7:
    if rep % 2 != 0:
        count_down(work_sec)
        label_1.config(text="Work Time", fg=PINK)
    # if rep 8:
    elif rep % 8 == 0:
        count_down(long_break_sec)
        label_1.config(text="Break Time", fg=RED)
    # if rep is 2/4/6:
    elif rep % 2 == 0:
        count_down(short_break_sec)
        label_1.config(text="Break Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(rep/2)):
            mark += "✔"
        label_2.config(text=mark)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_1 = Button(text="Start", command=start_timer)
button_1.grid(column=0, row=2)

button_2 = Button(text="Reset", command=reset_timer)
button_2.grid(column=2, row=2)

label_1 = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label_1.grid(column=1, row=0)

label_2 = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, pady=30)
label_2.grid(column=1, row=3)

window.mainloop()
