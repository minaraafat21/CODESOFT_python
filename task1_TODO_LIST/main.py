from tkinter import *

root = Tk()

root.title("To DO LIST")
root.geometry("400x800")
label1 = Label(root, text="Welcome to your To Do List", font=("Arial", 16), fg="green")
label1.pack()
label2 = Label(root, text="Enter your task", font=("Arial", 12))
label2.pack()


####################
def myClick():
    myLabel = Label(root, text=e.get(), font=("Arial", 12))
    myLabel.pack()


myButton = Button(root, text="Add Task", font=("Arial", 12), fg="green", command=myClick)
myButton.pack()

e = Entry(root, width=20, )
e.insert(50, "Enter your task")
e.pack()


root.mainloop()
