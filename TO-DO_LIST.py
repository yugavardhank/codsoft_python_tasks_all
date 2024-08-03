import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = {}

        self.task_label = tk.Label(root, text="Enter Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks[task] = "Pending"
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()
            messagebox.showinfo("Task Added", f'Task "{task}" added with status Pending.')

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.task_listbox.get(selected_task_index)
            if selected_task in self.tasks:
                self.tasks[selected_task] = "Completed"
                self.update_task_listbox()
                messagebox.showinfo("Task Completed", f'Task "{selected_task}" marked as Completed.')
        else:
            messagebox.showerror("Error", "No task selected.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.task_listbox.get(selected_task_index)
            if selected_task in self.tasks:
                del self.tasks[selected_task]
                self.update_task_listbox()
                messagebox.showinfo("Task Removed", f'Task "{selected_task}" removed.')
        else:
            messagebox.showerror("Error", "No task selected.")

    def view_tasks(self):
        if self.tasks:
            tasks_str = "\n".join([f'{task}: {status}' for task, status in self.tasks.items()])
            messagebox.showinfo("To-Do List", tasks_str)
        else:
            messagebox.showinfo("To-Do List", "Your To-Do list is empty.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Usage
root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()