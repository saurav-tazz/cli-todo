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
            option = int(input(f"{prompt} {f'(1)' if low == high else f'({low}-{high})'}: "))
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

def count_tasks(tasks):
    count = 0
    if not tasks:
        raise ValueError("Your ToDo list is empty")
    for task in tasks:
        count += 1
    return count

def mark_task(tasks, number):
    """add mark_task(tasks, number)"""
    for i, task in enumerate(tasks, start = 1):
        if i == number:
            task["done"] = True
            return

def delete_task(tasks, number):
    """Task to be deleted"""
    for i, task in enumerate(tasks, start = 1):
        if i == number:
            tasks.remove(task)
            return
    

def start_app():
    tasks = []
    print("="*20)
    print("CLI TODO APP")
    print("="*20)
    while True:
        print("\nMenu")
        print("1. Add\n2. View\n3. Mark\n4. Delete\n5. Quit")
        select = get_int("Enter option", 1, 5)
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
            '''mark task'''
            try:
                total = count_tasks(tasks)
            except ValueError as e:
                print(e)
            else:
                show_task(tasks)
                number = get_int("Enter the task you want to mark", 1, total)
                mark_task(tasks, number)
                print("Marked Task Done.")

        elif select == 4:
            '''delete'''
            try:
                total = count_tasks(tasks)
            except ValueError as e:
                print(e)
            else:
                show_task(tasks)
                number = get_int("Enter the task you want to delete", 1, total)
                delete_task(tasks, number)
                print("Deleted Task.")
        else:
            break

start_app()