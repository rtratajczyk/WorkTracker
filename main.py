'''A small Python program for purposes of time tracking of various tasks, for instance at work.
Developed by Rafał Ratajczyk.'''

import tkinter as tk
import tkinter.ttk
import time


class Task:
    """The Task class. Its init function creates all the necessary variables and tkinter widgets."""
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.is_tracked = False
        self.recordedTime = 0
        self.deleted = False
        self.NameLabel = tk.Label(master=frame, text=self.name)
        self.TimeLabel = tk.Label(master=frame, text="0h : 0m : 0s")
        self.RadioButton = tk.Radiobutton(master=frame, value=rows, variable=var, command=lambda a=self.number: select(a))
        self.DeleteButton = tk.Button(master=frame, text="X", command=lambda: delTask(self.number))


def onReturnKey(event):
    """An event listener that allows to add a task by pressing the Return key. Needs the positional event argument."""
    addTask()


def redrawTaskList():
    """A function which reorganizes the tasks[] list after one of them is deleted.
    Also redefines lambda functions of the remaining tasks' buttons, which is vital for proper further operations."""
    global rows
    global tasks
    global activeTask

    num = 0
    print("Redrawing list!")
    for t in tasks:
        t.number = num
        if t.is_tracked:
            activeTask = t.number
            print("ActiveTask renumbered.")
        t.DeleteButton.configure(command=lambda a=num: delTask(a))
        t.RadioButton.configure(command=lambda a=num: select(a))
        # print("The new number of Task named " + t.name + " is " + str(t.number))
        num += 1
    rows = num + 5


def delTask(number):
    """A function that deletes all widgets of a task, removes it from the tasks[] list and calls the redrawTaskList()
    function to reorganize the list."""
    global tasks
    global rows
    print("Deleting Task number: " + str(number) + ", while the current highest index of tasks[] is " + str(len(tasks)-1))
    if tasks[number].is_tracked:
        timeStop()
    tasks[number].NameLabel.destroy()
    tasks[number].TimeLabel.destroy()
    tasks[number].RadioButton.destroy()
    tasks[number].DeleteButton.destroy()
    del tasks[number]
    redrawTaskList()
    if number < activeTask:
        updateLoop(activeTask)


def timeConvert(sec):
    """A function for easy conversion of seconds into hours, minutes & seconds format.
    Returns a nicely formatted string."""
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    # print("{0}:{1}:{2}".format(int(hours), int(mins), sec))
    return "{0}h : {1}m : {2}s".format(int(hours), int(mins), int(sec))


def timeStart(task_number):
    """A function that starts time tracking for a task of the given number."""
    global activeTask
    global start_time
    global tasks
    global counter

    if tasks[task_number].is_tracked:
        tasks[task_number].RadioButton.deselect()
        return
    else:
        counter = 0
        start_time = time.time()
        activeTask = task_number
        tasks[task_number].is_tracked = True
        print("Tracking started for Task: " + tasks[activeTask].name)
        updateLoop(activeTask)


def updateLoop(task_number):
    """A looping function which allows for real-time updating of the time label of a task."""
    global tasks
    global counter

    def update():
        try:
            if tasks[task_number].is_tracked:
                global counter
                tasks[task_number].TimeLabel.configure(text=str(timeConvert(tasks[task_number].recordedTime)))
                tasks[task_number].TimeLabel.after(1000, update)
                counter += 1
                tasks[task_number].recordedTime += 1
        except IndexError:
            print("UpdateLoop IndexError!")
            redrawTaskList()
            return
    update()


def timeStop():
    """A function for easy setting of the is_tracked flag of a task to False."""
    global stop_time
    global tasks
    global counter
    #stop_time = time.time()
    for t in tasks:
        if t.is_tracked:
            tasks[activeTask].is_tracked = False

    # elapsed_time = timeConvert(stop_time-start_time)
    '''for t in tasks:
        if t.is_tracked:
            t.is_tracked = False
            try:
                t.recordedTime += (stop_time-start_time)
                t.TimeLabel.configure(text=str(timeConvert(t.recordedTime)))
            except IndexError:
                return'''
    # print("Tracking stopped. Lapsed time is: " + elapsed_time)


def select(task_number):
    """A function that handles the behavior of RadioButtons."""
    global first_count
    # global activeTask
    global tasks

    if not first_count:
        timeStop()
    else:
        first_count = False
    if task_number == activeTask:
        return
    else:
        timeStart(task_number)
    # tasks[task_number].is_tracked = True


def addTask():
    """A function for adding tasks to the tasks[] list. Pulls the name from the TaskCreationEntry entry, works only if
    the entry is not empty. Also grids all widgets of the new task to the frame."""

    if TaskCreationEntry.get() == "":
        return
    global rows
    global tasks
    print("putting new task in row:" + str(rows))
    tasks.append(Task(TaskCreationEntry.get(), len(tasks)))
    TaskCreationEntry.delete(0, tk.END)
    tasks[-1].NameLabel.grid(row=rows, column=0)
    tasks[-1].TimeLabel.grid(row=rows, column=1)
    tasks[-1].RadioButton.grid(row=rows, column=2)
    tasks[-1].DeleteButton.grid(row=rows, column=3)
    rows += 1


"""Main constant elements of the window are initialized and gridded below. Global variables are defined."""

window = tk.Tk()
window.title("WorkTracker")
var = tk.IntVar()
frame = tk.Frame(master=window)
frame.pack()

tasks = []
rows = 4
activeTask = -1
start_time = 0
stop_time = 0
first_count = True
counter = 0

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

# StopBtn = tk.Button(master=frame, text="Stop tracking", command=timeStop)
# StopBtn.grid(row=1, column=3)

NameTag = tk.Label(master=frame, text="Task name")
NameTag.grid(row=2, column=0)

ElapsedTag = tk.Label(master=frame, text="Recorded time")
ElapsedTag.grid(row=2, column=1)

TrackedTag = tk.Label(master=frame, text="Track")
TrackedTag.grid(row=2, column=2)

DeleteTag = tk.Label(master=frame, text="Delete")
DeleteTag.grid(row=2, column=3)

Separator = tkinter.ttk.Separator(master=frame)
Separator.grid(row=3, column=0, columnspan=4, sticky="ew")


window.mainloop()
