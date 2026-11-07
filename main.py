def view_task():
    """view task"""

def show_task(tasks):
    print("ToDo List")
    for i, task in enumerate(tasks, start = 1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task["title"]}")
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

def start_app():
    print("="*20)
    print("CLI TODO APP")
    print("="*20)
    while True:
        print("1. Add\n2. View\n3. Quit")
        select = get_int("Enter option", 1, 3)
        if select == 1:
            add_task(tasks, "Buy a Lamborghini")
        elif select == 2:
            show_task(tasks)
        elif select == 3:
            break

task = {"title" : "Buy Milk", "done" : False}
tasks = [task, {"title" : "Read chapter 3", "done" : True}]

start_app()