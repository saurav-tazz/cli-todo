def view_task():
    """view task"""

def show_task(tasks):
    if not tasks:
        print("Sorry your ToDo list is empty.")
        print()
        return
    print("ToDo List")
    for i, task in enumerate(tasks, start = 1):
        task["title"] = task["title"].strip()
        if task["title"] == "":
            continue
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")
    print()

def add_task(tasks, title):
    """Task to be added"""
    title = title.strip()
    if title == "":
        print("Cannot add an empty task.")
    else:
        tasks.append({"title": title, "done": False})

def mark_task():
    """mark task"""

def delete_task():
    """delete task"""

def get_int(prompt, low, high):
    while True:
        try:
            option = int(input(f"{prompt} ({low}-{high}): "))
        except ValueError:
            print("Error: Expected a Number")
        else:
            if option in range(low, high + 1):
                return option
            else:
                print(f"Select from {low} to {high}")

def get_task():
    title = input("Enter new task: ").strip()
    if title == "":
        print("Tasks cannot be empty")
    elif len(title) > 200:
        print("Maximum 200 Characters")
    else:
        return title



def start_app():
    print("="*20)
    print("CLI TODO APP")
    print("="*20)
    while True:
        print("1. Add\n2. View\n3. Quit")
        select = get_int("Enter option", 1, 3)
        if select == 1:
            title = get_task()
            add_task(tasks, title)
        elif select == 2:
            show_task(tasks)
        elif select == 3:
            break

task = {"title" : "Buy Milk", "done" : False}
tasks = [task, {"title" : "Read chapter 3", "done" : True}]

start_app()