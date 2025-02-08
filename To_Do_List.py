import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status TEXT)''')
conn.commit()

# Function to fetch tasks from the database
def load_tasks():
    listbox.delete(0, tk.END)  # Clear listbox
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        task_display = f"{'✅' if row[2] == 'completed' else '❌'} {row[1]}"
        listbox.insert(tk.END, task_display)

# Function to add a new task
def add_task():
    task_text = task_entry.get()
    if task_text:
        cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task_text, "pending"))
        conn.commit()
        task_entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task = listbox.get(tk.ACTIVE)
        if selected_task:
            task_name = selected_task[2:]  # Remove emoji
            cursor.execute("UPDATE tasks SET status = 'completed' WHERE task = ?", (task_name,))
            conn.commit()
            load_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

# Function to delete a task
def delete_task():
    try:
        selected_task = listbox.get(tk.ACTIVE)
        if selected_task:
            task_name = selected_task[2:]  # Remove emoji
            cursor.execute("DELETE FROM tasks WHERE task = ?", (task_name,))
            conn.commit()
            load_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark Completed", command=complete_task)
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Load existing tasks from the database
load_tasks()

# Run the Tkinter event loop
root.mainloop()
