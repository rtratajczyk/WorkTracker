import tkinter as tk
import tkinter.ttk
import time

'''BACKLOG: fix recording time for deleted tasks, somehow do time updating with label.after()'''


window = tk.Tk()
window.title("WorkTracker")
frame = tk.Frame(master=window)
frame.pack()


class Task:
    """The Task class"""
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.is_tracked = False
        self.recordedTime = 0
        self.deleted = False
        self.NameLabel = tk.Label(master=frame, text=self.name)
        self.TimeLabel = tk.Label(master=frame, text=self.recordedTime)
        self.RadioButton = tk.Radiobutton(master=frame, value=rows, variable=var, command=lambda a=self.number: select(a))
        self.DeleteButton = tk.Button(master=frame, text="X", command=lambda: delTask(self.number))


def onReturnKey(event):
    addTask()


def redrawTasklist():
    global rows
    global tasks

    num = 0
    rows = 4
    for t in tasks:
        t.number = num
        t.DeleteButton.configure(command=lambda a=num: delTask(a))
        t.RadioButton.configure(command=lambda a=num: select(a))
        print("The new number of Task named " + t.name + " is " + str(t.number))
        num += 1


def delTask(number):
    global tasks
    print("Deleting Task number: " + str(number) + ", while the current highest index of tasks[] is " + str(len(tasks)-1))
    if tasks[number].is_tracked:
        timeStop()
    tasks[number].NameLabel.destroy()
    tasks[number].TimeLabel.destroy()
    tasks[number].RadioButton.destroy()
    tasks[number].DeleteButton.destroy()
    del tasks[number]
    redrawTasklist()


tasks = []
rows = 4
var = tk.IntVar()
activeTask = 0
running = False
start_time = 0
stop_time = 0
first_count = True


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    # print("{0}:{1}:{2}".format(int(hours), int(mins), sec))
    return "{0}h : {1}m : {2}s".format(int(hours), int(mins), int(sec))


def timeStart(task_number):
    global activeTask
    global start_time
    global tasks
    start_time = time.time()
    activeTask = task_number
    tasks[task_number].is_tracked = True
    print("Tracking started for Task: " + tasks[activeTask].name)


def timeCounterLabel(label):
    global activeTask
    global stop_time
    stop_time = time.time()
    # label.after(1000, )


def timeStop():
    global stop_time
    global tasks
    stop_time = time.time()
    elapsed_time = time_convert(stop_time-start_time)

    for t in tasks:
        if t.is_tracked:
            t.is_tracked = False
            try:
                t.recordedTime += (stop_time-start_time)
                t.TimeLabel.config(text=str(time_convert(t.recordedTime)))
            except IndexError:
                return
    print("Tracking stopped. Lapsed time is: " + elapsed_time)


def select(task_number):
    global first_count
    global activeTask

    if not first_count:
        timeStop()
    else:
        first_count = False
    timeStart(task_number)
    # tasks[task_number].is_tracked = True



def addTask():

    if TaskCreationEntry.get() == "":
        return
    global rows

    tasks.append(Task(TaskCreationEntry.get(), len(tasks)))
    # tasks[-1].number = len(tasks)
    tasks[-1].NameLabel.grid(row=rows, column=0)
    tasks[-1].TimeLabel.grid(row=rows, column=1)
    tasks[-1].RadioButton.grid(row=rows, column=2)
    tasks[-1].DeleteButton.grid(row=rows, column=3)
    rows += 1


WelcomeLabel = tk.Label(master=frame, text="Welcome to WorkTracker, alpha version!")
WelcomeLabel.grid(row=0, column=0)

TaskCreationLabel = tk.Label(master=frame, text="Input name of a new Task to track:")
TaskCreationLabel.grid(row=1, column=0)

TaskCreationEntry = tk.Entry(master=frame)
TaskCreationEntry.grid(row=1, column=1)
TaskCreationEntry.insert(0, "New Task")
TaskCreationEntry.bind('<Return>', onReturnKey)

TaskCreationBtn = tk.Button(master=frame, text="Add", command=addTask)
TaskCreationBtn.grid(row=1, column=2)

StopBtn = tk.Button(master=frame, text="Stop tracking", command=timeStop)
StopBtn.grid(row=1, column=3)

NameTag = tk.Label(master=frame, text="Task name")
NameTag.grid(row=2, column=0)

ElapsedTag = tk.Label(master=frame, text="Recorded time")
ElapsedTag.grid(row=2, column=1)

TrackedTag = tk.Label(master=frame, text="Track")
TrackedTag.grid(row=2, column=2)

DeleteTag = tk.Label(master=frame, text="Delete Task")
DeleteTag.grid(row=2, column=3)

Separator = tkinter.ttk.Separator(master=frame)
Separator.grid(row=3, column=0, columnspan=4, sticky="ew")


window.mainloop()
