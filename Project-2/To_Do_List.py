import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        file.writelines([task + "\n" for task in tasks])

# Add a task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "No task selected!")

# Save tasks and close the application
def exit_app():
    tasks = task_listbox.get(0, tk.END)
    save_tasks(tasks)
    root.destroy()

# Load tasks into the Listbox on startup
def load_into_listbox():
    for task in load_tasks():
        task_listbox.insert(tk.END, task)

# Main GUI setup
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Entry widget to add tasks
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons for actions
add_button = tk.Button(root, text="Add Task", command=add_task, width=20)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=20)
delete_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=15)
task_listbox.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Save and Exit", command=exit_app, width=20)
exit_button.pack(pady=10)

# Load tasks into the listbox at startup
load_into_listbox()

# Run the application
root.mainloop()
