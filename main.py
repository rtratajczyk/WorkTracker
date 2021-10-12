import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("WorkTracker")
# window.columnconfigure

rows = 1


def addTask():
    NewTaskName = NewTaskEntry["text"]
    NewTask = tk.Label(master=frame, text=NewTaskName)
    NewTask.grid(row=1, column=0)
    NewTaskEntry.delete(0, tk.END)

    NewTaskTimer = tk.Label(master=frame, text="00:00:00")
    NewTaskTimer.grid(row=1, column=1)

    NewTaskRadioBtn = tk.Radiobutton(master=frame)
    NewTaskRadioBtn.grid(row=1, column=2)


frame = tk.Frame(master=window)
frame.pack()

NewTaskLabel = tk.Label(master=frame, text="Input name of a new task to track:")
NewTaskLabel.grid(row=0, column=0, sticky="e")

NewTaskEntry = tk.Entry(master=frame)
NewTaskEntry.grid(row=0, column=1)

NewTaskAddBtn = tk.Button(master=frame, text="Add", command=addTask)
NewTaskAddBtn.grid(row=0, column=2)

window.mainloop()
