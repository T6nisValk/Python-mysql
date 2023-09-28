import crud
import tkinter as tk
from tkinter import messagebox


def refresh():
    display_tasks_lb.delete(0, tk.END)
    display_lists_lb.delete(0, tk.END)
    for i, list in enumerate(crud.select_lists()):
        display_lists_lb.insert(i, f"ID: {list.list_id}, Name: {list.title}")
    for i, task in enumerate(crud.select_tasks()):
        display_tasks_lb.insert(
            i,
            f"ID: {task.item_id}, "
            f"Name: {task.name}, "
            f"Status: {'Completed' if task.state else 'Not completed'}, "
            f"List ID: {task.list_id}",
        )


def delete_list():
    if display_lists_lb.curselection():
        list_id = display_lists_lb.selection_get().split(" ")[1].rstrip(",")
        name = crud.select_list(int(list_id))
        crud.delete_list(int(list_id))
        refresh()
        messagebox.showinfo(
            title="Info", message=f"List {name.title} and all it's tasks successfully deleted."
        )
    else:
        messagebox.showerror(title="Error", message="No list selected")


def delete_task():
    if display_tasks_lb.curselection():
        task_id = display_tasks_lb.selection_get().split(" ")[1].rstrip(",")
        name = crud.select_task(int(task_id))
        crud.delete_task(int(task_id))
        refresh()
        messagebox.showinfo(title="Info", message=f"Task {name.name} successfully deleted.")
    else:
        messagebox.showerror(title="Error", message="No task selected")


def create_list():
    if len(name_input.get()) >= 3:
        name = name_input.get()
        name_input.delete(0, tk.END)
        crud.create_todo_list(name)
        refresh()
        messagebox.showinfo(title="Info", message=f"List '{name}' successfully created!")
    else:
        messagebox.showwarning(title="Warning", message="Name should be at least 3 characters.")


def create_task():
    if display_lists_lb.curselection():
        if len(name_input.get()) >= 3:
            selected_list_id = display_lists_lb.selection_get().split(" ")[1].rstrip(",")
            list_name = crud.select_list(selected_list_id)
            name = name_input.get()
            name_input.delete(0, tk.END)
            crud.create_task(selected_list_id, name)
            refresh()
            messagebox.showinfo(
                title="Info", message=f"Task '{name}' for '{list_name.title}' successfully created!"
            )
        else:
            messagebox.showwarning(title="Warning", message="Name should be at least 3 characters.")
    else:
        messagebox.showerror(title="Error", message="No list selected")


def task_complete():
    if display_tasks_lb.curselection():
        selected_task_id = display_tasks_lb.selection_get().split(" ")[1].rstrip(",")
        crud.select_task(selected_task_id)
        task = crud.select_task(selected_task_id)
        task.state = True
        refresh()
        messagebox.showinfo(title="Info", message=f"{task.name} set to 'Completed'")

    else:
        messagebox.showerror(title="Error", message="No task selected")


def task_uncomplete():
    if display_tasks_lb.curselection():
        selected_task_id = display_tasks_lb.selection_get().split(" ")[1].rstrip(",")
        task = crud.select_task(selected_task_id)
        task.state = False
        refresh()
        messagebox.showinfo(title="Info", message=f"{task.name} set to 'Not Completed'")
    else:
        messagebox.showerror(title="Error", message="No task selected")


def display_info():
    messagebox.showinfo(
        title="Help info",
        message="Welcome to the TODO APP!\n"
        "- To see currently created lists and tasks, hit the refresh button.\n"
        "- To delete a list or a task, first select a list or a task from the available lists/tasks.\n"
        "- To mark a task Completed or Not Completed, first select a task from the available tasks.\n"
        "- To create a list, enter a name in the input field and click on the Create list button.\n"
        "- To create a task, first select a list you want to create a task for and then enter the name "
        "in the input field and click Create task button.",
    )


app = tk.Tk()
app.title("Todo App")
app.geometry("400x650")
app.config(background="TEAL")

menubar = tk.Menu(app)
app.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff="off")
file_menu.add_command(label="Exit", command=app.destroy)
menubar.add_cascade(label="File", menu=file_menu)

info_menu = tk.Menu(menubar, tearoff="off")
info_menu.add_command(label="Help", command=lambda: display_info())
menubar.add_cascade(label="Help", menu=info_menu)

lists_label = tk.Label(app, text="Available lists.", justify="left", background="TEAL")
lists_label.pack(padx=5, pady=5, anchor="w")

display_lists_lb = tk.Listbox(app, width=38)
display_lists_lb.pack(fill="x", padx=5)

tasks_label = tk.Label(app, text="Available tasks.", justify="left", background="TEAL")
tasks_label.pack(padx=5, pady=5, anchor="w")

display_tasks_lb = tk.Listbox(app, width=39)

display_tasks_lb.pack(padx=5, fill="x")

refresh_data = tk.Button(
    app, text="Refresh lists and tasks", command=lambda: refresh(), borderwidth=5, relief="raised"
)
refresh_data.pack(padx=5, pady=5, fill="x")

delete_list_button = tk.Button(
    app, text="Delete list", command=lambda: delete_list(), borderwidth=5, relief="raised"
)
delete_list_button.pack(padx=5, fill="x")

delete_task_button = tk.Button(
    app, text="Delete task", command=lambda: delete_task(), borderwidth=5, relief="raised"
)
delete_task_button.pack(pady=5, padx=5, fill="x")

complete_button = tk.Button(
    app,
    text="Mark task as 'Completed'",
    command=lambda: task_complete(),
    borderwidth=5,
    relief="raised",
)
complete_button.pack(padx=5, fill="x")

uncomplete_button = tk.Button(
    app,
    text="Mark task as 'Not Completed'",
    command=lambda: task_uncomplete(),
    borderwidth=5,
    relief="raised",
)
uncomplete_button.pack(padx=5, pady=5, fill="x")


grid_frame = tk.Frame(app, background="TEAL")
grid_frame.pack()

input_label = tk.Label(grid_frame, text="User input:", background="TEAL")
input_label.grid(row=1, column=0)

name_input = tk.Entry(grid_frame, borderwidth=2, relief="sunken")
name_input.grid(row=1, column=1)

list_button = tk.Button(
    grid_frame, text="Create list", command=lambda: create_list(), borderwidth=5, relief="raised"
)
list_button.grid(row=1, column=2, padx=5)

task_button = tk.Button(
    grid_frame, text="Create task", command=lambda: create_task(), borderwidth=5, relief="raised"
)
task_button.grid(row=1, column=3)


if __name__ == "__main__":
    app.mainloop()
