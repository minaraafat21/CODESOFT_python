import tkinter as tk
from tkinter import *


def change_label_text(new_text):
    label1.config(text=label1.cget("text") + new_text)


def clear_label_text():
    label1.config(text="")
    label2.config(text="")


def myEval(expression):
    try:
        result = eval(expression)
        label2.config(text=result)
    except Exception as e:
        label2.config(text=" ERROR: " + str(e))


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#17181A")

myBlack = "#17181A"
myGrey = "#303136"
myBlue = "#005DB2"

label1 = tk.Label(root, text="", font=("Arial", 24), bg=myBlack, fg="#5F5F60")
label1.grid(row=2, column=0, columnspan=15, sticky="e")

label2 = tk.Label(root, text="", bg=myBlack, font=("Arial", 28), fg="white")
label2.grid(row=4, column=0, columnspan=15, sticky="e")

label3 = tk.Label(root, text="\n \n \n \n \n", bg=myBlack, font=("Arial", 12))
label3.grid(row=0, column=0, rowspan=3)



# Create buttons and shift them down by 4 rows
button1 = Button(root, text="1", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("1"))
button1.grid(row=9, column=0)

button2 = Button(root, text="2", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("2"))
button2.grid(row=9, column=1)

button3 = Button(root, text="3", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("3"))
button3.grid(row=9, column=2)

button4 = Button(root, text="4", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("4"))
button4.grid(row=8, column=0)

button5 = Button(root, text="5", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("5"))
button5.grid(row=8, column=1)

button6 = Button(root, text="6", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("6"))
button6.grid(row=8, column=2)

button7 = Button(root, text="7", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("7"))
button7.grid(row=7, column=0)

button8 = Button(root, text="8", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("8"))
button8.grid(row=7, column=1)

button9 = Button(root, text="9", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("9"))
button9.grid(row=7, column=2)

button0 = Button(root, text="0", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("0"))
button0.grid(row=10, column=1)

button_dot = Button(root, text=".", width=5, height=3, bg=myGrey, fg=myBlue, command=lambda: change_label_text("."))
button_dot.grid(row=10, column=0)

button_plus = Button(root, text="+", width=5, height=3, bg=myBlue, command=lambda: change_label_text("+"))
button_plus.grid(row=6, column=3)

butotn_mince = Button(root, text="-", width=5, height=3, bg=myBlue, command=lambda: change_label_text("-"))
butotn_mince.grid(row=7, column=3)

button_times = Button(root, text="*", width=5, height=3, bg=myBlue, command=lambda: change_label_text("*"))
button_times.grid(row=8, column=3)

button_divide = Button(root, text="/", width=5, height=3, bg=myBlue, command=lambda: change_label_text("/"))
button_divide.grid(row=9, column=3)

button_equal = Button(root, text="=", width=16, height=3, bg=myBlue, command=lambda: myEval(label1.cget("text")))
button_equal.grid(row=10, column=2, columnspan=2)

button_clear = Button(root, text="Clear", width=5, height=3,fg="#9E9E9F", bg="#5F5F60", command=clear_label_text)
button_clear.grid(row=6, column=2)

root.rowconfigure(5, minsize=60)
for i in range(6, 10):
    root.rowconfigure(i, minsize=75)

for i in range(0, 4):
    root.columnconfigure(i, minsize=100)

root.mainloop()
