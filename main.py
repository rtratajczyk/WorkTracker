import tkinter as tk
import time

window = tk.Tk()
window.title("WorkTracker")
# window.columnconfigure
frame = tk.Frame(master=window)
frame.pack()


class task:
    """The task class"""
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.row = number + 2
        self.is_tracked = False
        self.recordedTime = 0
        self.deleted = False
        self.NameLabel = tk.Label(master=frame, text=self.name)
        self.TimeLabel = tk.Label(master=frame, text=self.recordedTime)
        self.RadioButton = tk.Radiobutton(master=frame, value=rows, variable=var, command=select)
        self.DeleteButton = tk.Button(master=frame, text="Delete task", command=lambda a=self.number: delTask(a))


def redrawTasklist():
    global rows
    global tasks
    global redrawn_tasks
    rows = 2
    for t in tasks:
        if t.deleted:
            return
        else:
            t.NameLabel.grid(row=rows, column=0)
            t.TimeLabel.grid(row=rows, column=1)
            t.RadioButton.grid(row=rows, column=2)
            t.DeleteButton.grid(row=rows, column=3)
            rows +=1


def delTask(number):
    global tasks
    print("Delete task named "+tasks[number].name + " number " + str(number))
    tasks[number].deleted = True
    #redrawTasklist()


tasks = []
redrawn_tasks = []
rows = 2
var = tk.IntVar()
activeTask = 0
start_time = 0
stop_time = 0
first_count = True



def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    #print("{0}:{1}:{2}".format(int(hours), int(mins), sec))
    return "{0}:{1}:{2}".format(int(hours), int(mins), int(sec))


def timeStart(taskNumber):
    global activeTask
    global start_time
    start_time = time.time()
    activeTask = taskNumber
    print("Tracking started for task: " + tasks[activeTask].name)


def timeStop(taskNumber):
    global stop_time
    stop_time = time.time()
    elapsed_time = time_convert(stop_time-start_time)
    tasks[taskNumber].recordedTime += (stop_time-start_time)
    tasks[taskNumber].TimeLabel.config(text=str(time_convert(tasks[taskNumber].recordedTime)))
    #for widget in slaves:
    print("Tracking stopped. Lapsed time is: " + elapsed_time)


def select():
    global first_count
    global rows
    global activeTask

    taskNumber = activeTask
    if not first_count:
        timeStop(taskNumber)
    else:
        first_count = False
    taskNumber = var.get()
    timeStart(taskNumber)
    tasks[taskNumber].is_tracked = True
    activeTask = taskNumber


def addTask():

    if TaskCreationEntry.get() == "":
        return
    global rows

    tasks.append(task(TaskCreationEntry.get(), len(tasks)))
    #tasks[-1].number = len(tasks)
    tasks[-1].NameLabel.grid(row=rows, column=0)
    tasks[-1].TimeLabel.grid(row=rows, column=1)
    tasks[-1].RadioButton.grid(row=rows, column=2)
    tasks[-1].DeleteButton.grid(row=rows, column=3)
    rows += 1


WelcomeLabel = tk.Label(master=frame, text="Welcome to WorkTracker, alpha version!")
WelcomeLabel.grid(row=0, column=0)

TaskCreationLabel = tk.Label(master=frame, text="Input name of a new task to track:")
TaskCreationLabel.grid(row=1, column=0)

TaskCreationEntry = tk.Entry(master=frame)
TaskCreationEntry.grid(row=1, column=1)
TaskCreationEntry.insert(0, "New Task")

TaskCreationBtn = tk.Button(master=frame, text="Add", command=addTask)
TaskCreationBtn.grid(row=1, column=2)

window.mainloop()
