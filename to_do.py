import tkinter as tk
root=tk.Tk()
root.title("python GUI Calculator")
root.geometry("600x800")
root.config(bg="white")

def add_task():
    t=task.get()
    list_items.insert(tk.END, t)
    task.delete(0, tk.END)

def delete_task():
    temp = list_items.curselection()
    list_items.delete(temp)

heading=tk.Label(root,text="To Do List",font=("Calibri",25),bg="skyblue",fg="blue")
heading.pack(pady=10)

heading2=tk.Label(root,text="organize your day",font=("Calibri",20),bg="skyblue",fg="darkblue")
heading2.pack(pady=10)

task=tk.Entry(root,font=("Calibri",20),bg="white",fg="blue")
task.pack(pady=10)

add_button=tk.Button(root,text="Add Task",font=("Calibri",20),command=add_task,bg="skyblue",fg="black")
add_button.pack(pady=10)

list_items= tk.Listbox(root, font=("Calibri", 20),bg="white",fg="blue")
list_items.pack(pady=10)

del_but=tk.Button(root,text="delete task",font=("Calibri",20),command=delete_task,bg="skyblue",fg="black")
del_but.pack(pady=10)


root.mainloop()