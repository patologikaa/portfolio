from tkinter import *
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
def reset_game():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="")
    window.after_cancel(timer)
    label.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_game():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps %8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps %2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    if count>0:
        global  timer
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        start_game()
        mark = ""
        for x in range (reps//2):
            mark+="✔"
        text.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))




label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)



text = Label(text= "", fg=GREEN, bg=YELLOW)

start = Button(text="Start", command=start_game)
reset = Button(text="Reset", command=reset_game, highlightthickness=0)




label.grid(column=2,row=0)
canvas.grid(column=2,row= 2)
start.grid(column=1, row= 3)
reset.grid(column=3, row= 3)
text.grid(column=2, row=4)
window.mainloop()
