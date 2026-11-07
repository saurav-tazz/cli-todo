def view_task():
    """view task"""

def show_task(tasks):
    print("ToDo List")
    for i, task in enumerate(tasks, start = 1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task["title"]}")
    print()

def add_task():
    """Task to be added"""

def mark_task():
    """mark task"""

def delete_task():
    """delete task"""


task = {"title" : "Buy Milk", "done" : False}
tasks = [task, {"title" : "Read chapter 3", "done" : True}]

show_task(tasks)