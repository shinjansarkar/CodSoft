import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create main application window
app = tk.Tk()
app.title("To-Do List")

# Set the background color for the main window
app.configure(bg="lightblue")

# Create an input field and buttons
entry = tk.Entry(app, width=40, bg="white")
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", width=30, command=add_task, bg="green", fg="white")
add_button.pack(pady=5)

remove_button = tk.Button(app, text="Remove Task", width=30, command=remove_task, bg="red", fg="white")
remove_button.pack(pady=5)

# Create a listbox to display tasks
task_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40, height=10, bg="white")
task_list.pack(pady=10)

# Start the application
app.mainloop()
