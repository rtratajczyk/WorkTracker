import tkinter as tk
import time

window = tk.Tk()
window.title("WorkTracker")
# window.columnconfigure


class task:
    """The task class"""
    def __init__(self, name, row, is_tracked, recordedTime):
        self.name = name
        self.row = row
        self.isTracked = False
        self.recordedTime = 0


tasks = ['dummy', 'dummy']  # creating a list for storing tasks with two dummy tasks (because first two rows are taken)
rows = 2
var = tk.IntVar()


def timeTrack():
    print(time.time())

def select():
    taskNumber = var.get()
    tasks[taskNumber].is_tracked = True
    if tasks[taskNumber].is_tracked:
        timeTrack()
        print("Task " + tasks[taskNumber].name + "is now tracked")



def delTask():
    print("DELETE TASK NUMBER "+ str(var.get()))


def addTask():

    if TaskCreationEntry.get() == "":
        return
    global rows
    tasks.append(task(TaskCreationEntry.get(), rows))
    NewTaskLabel = tk.Label(master=frame, text=TaskCreationEntry.get())
    NewTaskLabel.grid(row=rows, column=0)
    TaskCreationEntry.delete(0, tk.END)

    NewTaskTimer = tk.Label(master=frame, text="00:00:00")
    NewTaskTimer.grid(row=rows, column=1)

    '''
    TrackingLabel = tk.Label(master=frame, text = "Currently tracked:")
    TrackingLabel.grid(row = rows, column = 2)
    '''

    NewTaskRadioBtn = tk.Radiobutton(master=frame, value = rows, variable = var, command = select)
    NewTaskRadioBtn.grid(row=rows, column=3)

    KillTaskBtn = tk.Button(master=frame, text = "Delete task", command=delTask)
    KillTaskBtn.grid(row=rows, column = 4)

    rows += 1


frame = tk.Frame(master=window)
frame.pack()

WelcomeLabel = tk.Label(master=frame, text = "Welcome to WorkTracker, alpha version!")
WelcomeLabel.grid(row=0, column=0)

TaskCreationLabel = tk.Label(master=frame, text="Input name of a new task to track:")
TaskCreationLabel.grid(row=1, column=0)

TaskCreationEntry = tk.Entry(master=frame)
TaskCreationEntry.grid(row=1, column=1)
TaskCreationEntry.insert(0, "New Task")

TaskCreationBtn = tk.Button(master=frame, text="Add", command=addTask)
TaskCreationBtn.grid(row=1, column=2)

window.mainloop()
