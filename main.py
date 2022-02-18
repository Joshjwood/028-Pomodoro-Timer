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
reps = 0

timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    header_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps, ticks
    ticks = []
    reps = 0
    check_marks.config(text="".join(ticks))


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        header_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 8:
        ticks.append("✓")
        check_marks.config(text="".join(ticks))
        header_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        ticks.append("✓")
        check_marks.config(text="".join(ticks))
        header_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)

    if len(str(count_min)) == 1:
        count_min = "0" + str(count_min)



    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

header_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
header_label.grid(row=0,column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)



start_button = Button(text="Start",command=start_timer, fg="black", bg=YELLOW, highlightthickness=0)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",command=reset_timer, fg="black", bg=YELLOW, highlightthickness=0)
reset_button.grid(row=2,column=2)

ticks = []

check_marks = Label(text="".join(ticks), fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
check_marks.grid(column=1, row=3)


window.mainloop()