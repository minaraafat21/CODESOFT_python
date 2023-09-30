from tkinter import *


def on_checkbox_toggle(var, label):
    if var.get() == 1:
        label.config(text=strike(label.cget("text")))


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336' # Add a combining strike through character
    return result


def myClick():
    text = e.get()
    var = IntVar()
    checkbox = Checkbutton(frame, text=text, variable=var, font=('Copper Black'
                                                                 '', 16), bg='white')
    checkbox.pack(pady=10, anchor='w', padx=10)  # Align to the left
    checkbox.config(command=lambda var=var, label=checkbox: on_checkbox_toggle(var, label))
    checkboxes.append((var, checkbox))  # Keep track of the checkboxes


def clear_done_tasks():
    for var, checkbox in checkboxes:
        if var.get() == 1:
            checkbox.pack_forget()


# Create the main window
root = Tk()
root.title("To Do List")
root.geometry("450x800")
root.configure(bg='white')  # Set background color

label1 = Label(root, text="Welcome to your To Do List", font=("Arial", 16), fg="green", bg='white')
label1.pack()
label2 = Label(root, text="Enter your task", font=("Arial", 12), bg='white')
label2.pack()

# Create an entry widget
e = Entry(root)
e.pack(pady=10)
# Create a button to create checkboxes
myButton = Button(root, text="add task", command=myClick, bg='#4CAF50', fg='white', font=("Arial", 12))
myButton.pack(pady=5, padx=10)  # Adjust width and padding

# Create a frame to contain checkboxes
frame = Frame(root, bg='white')
frame.pack()



# Create a button to clear done tasks
clearButton = Button(root, text="Clear Done Tasks", command=clear_done_tasks, bg='#FF5722', fg='white', font=("Arial", 12))
clearButton.pack(pady=5, side='bottom', fill='x', padx=30, ipadx=20)  # Adjust width and padding

# Keep track of variables and checkboxes
checkboxes = []

# Start the main event loop
root.mainloop()
