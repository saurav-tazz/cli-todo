import json

def show_task(tasks):
    if not tasks:
        print("Sorry your ToDo list is empty.")
        return
    print("ToDo List")
    for i, task in enumerate(tasks, start = 1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")

def add_task(tasks):
    title = input("Enter new task: ").strip()
    if title == "":
        raise ValueError("Cannot add an empty task.")
    elif len(title) > 200:
        raise ValueError("Maximum 200 Characters")
    tasks.append({"title": title, "done": False})

def get_int(prompt, low, high):
    while True:
        try:
            option = int(input(f"{prompt} {f'({low})' if low == high else f'({low}-{high})'}: "))
        except ValueError:
            print("Error: Expected a Number")
        else:
            if option in range(low, high + 1):
                return option
            else:
                print(f"Select from {low} to {high}")

def count_tasks(tasks):
    if not tasks:
        raise ValueError("Sorry your ToDo list is empty.")
    return len(tasks)

def mark_task(tasks, number):
    total = count_tasks(tasks)
    if number not in range(1, total + 1):
        raise ValueError(f"Select from 1 to {total}")

    tasks[number - 1]["done"] = True

def delete_task(tasks, number):
    total = count_tasks(tasks)
    if number not in range(1, total + 1):
        raise ValueError(f"Select from 1 to {total}")
    tasks.pop(number - 1)

def save_tasks(tasks, filename = "tasks.json"):
    with open(filename, "w", encoding = "utf-8") as f:
        json.dump(tasks, f)

def load_tasks(filename = "tasks.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        return loaded
    except FileNotFoundError:
        return []
    
def start_app(filename):
    try:
        tasks = load_tasks(filename)
    except ValueError:
        print(f"Error: {filename} is damaged and could not be read.\nFix the file or delete it, then run the program again")
        return
    print("="*20)
    print("CLI TODO APP")
    print("="*20)
    while True:
        print("\nMenu")
        print("1. Add\n2. View\n3. Mark\n4. Delete\n5. Quit")
        select = get_int("Enter option", 1, 5)
        if select == 1:
            try:
                add_task(tasks)
                save_tasks(tasks, filename)
                print("\nTask Added Successfully!!!\n")
                
            except ValueError as e:
                print(e)

        elif select == 2:
            show_task(tasks)

        elif select == 3:
            try:
                total = count_tasks(tasks)
                show_task(tasks)
                number = get_int("Enter the task you want to mark", 1, total)
                mark_task(tasks, number)
                save_tasks(tasks, filename)
                print("\nMarked Task Done!!!")
                
            except ValueError as e:
                print(e)
            
        elif select == 4:
            try:
                total = count_tasks(tasks)
                show_task(tasks)
                number = get_int("Enter the task you want to delete", 1, total)
                delete_task(tasks, number)
                save_tasks(tasks, filename)
                print("\nDeleted Task!!!")
                
            except ValueError as e:
                print(e)

        elif select == 5:
            break

start_app("tasks.json")