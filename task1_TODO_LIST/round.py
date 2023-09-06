import tkinter as tk

# Function to handle button click event
def on_button_click():
    # Replace this function with your desired action
    print("Button clicked")

# Create the main application window
root = tk.Tk()
root.title("Rounded Button")

# Create a canvas widget to draw the rounded button
canvas = tk.Canvas(root, width=100, height=40, highlightthickness=0)
canvas.pack()

# Draw the rounded button using the canvas
button = canvas.create_oval(0, 0, 1000, 40, fill="blue")  # Adjust the size and color as needed

# Add a text label to the button
label = canvas.create_text(50, 20, text="Click Me", fill="white")

# Bind a click event to the button
canvas.tag_bind(button, "<Button-1>", lambda event: on_button_click())

root.mainloop()
