def show_task(tasks):
    if not tasks:
        print("Sorry your ToDo list is empty.")
        return
    print("ToDo List")
    for i, task in enumerate(tasks, start = 1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")

def add_task(tasks, title):
    """Task to be added"""
    title = title.strip()
    if title == "":
        raise ValueError("Cannot add an empty task.")
    elif len(title) > 200:
        raise ValueError("Maximum 200 Characters")
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
    title = input("Enter new task: ")
    return title



def start_app():
    tasks = []
    print("="*20)
    print("CLI TODO APP")
    print("="*20)
    while True:
        print("\nMenu")
        print("1. Add\n2. View\n3. Quit")
        select = get_int("Enter option", 1, 3)
        if select == 1:
            title = get_task()
            try:
                add_task(tasks, title)
                print("\nTask Added Successfully!!!\n")
            except ValueError as e:
                print(e)
        elif select == 2:
            show_task(tasks)
        elif select == 3:
            break


start_app()