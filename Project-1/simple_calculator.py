import tkinter as tk

# Button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Clear function
def clear():
    entry.delete(0, tk.END)

# Equal function
def calculate():
    try:
        result = eval(entry.get()) 
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window setup
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget
entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda x=text: button_click(x)
    tk.Button(root, text=text, width=6, height=2, command=action).grid(row=row, column=col)

root.mainloop()
