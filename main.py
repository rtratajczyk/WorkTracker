import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("WorkTracker")
# window.columnconfigure

rows = 2
var = tk.IntVar()


def delTask():
    print("DELETE!!")


def addTask():

    if NewTaskEntry.get() == "": return
    global rows
    NewTask = tk.Label(master=frame, text=NewTaskEntry.get())
    NewTask.grid(row=rows, column=0)
    NewTaskEntry.delete(0, tk.END)

    NewTaskTimer = tk.Label(master=frame, text="00:00:00")
    NewTaskTimer.grid(row=rows, column=1)

    '''
    TrackingLabel = tk.Label(master=frame, text = "Currently tracked:")
    TrackingLabel.grid(row = rows, column = 2)
    '''

    NewTaskRadioBtn = tk.Radiobutton(master=frame, value = rows, variable = var)
    NewTaskRadioBtn.grid(row=rows, column=3)

    KillTaskBtn = tk.Button(master=frame, text = "Delete task", command=delTask)
    KillTaskBtn.grid(row=rows, column = 4)

    rows += 1


frame = tk.Frame(master=window)
frame.pack()

WelcomeLabel = tk.Label(master=frame, text = "Welcome to WorkTracker, alpha version!")
WelcomeLabel.grid(row = 0, column = 0)

NewTaskLabel = tk.Label(master=frame, text="Input name of a new task to track:")
NewTaskLabel.grid(row=1, column=0, sticky="e")

NewTaskEntry = tk.Entry(master=frame)
NewTaskEntry.grid(row=1, column=1)
NewTaskEntry.insert(0, "New Task")

NewTaskAddBtn = tk.Button(master=frame, text="Add", command=addTask)
NewTaskAddBtn.grid(row=1, column=2)

window.mainloop()
