def view_task():
    """view task"""

def add_task():
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

tasks = [{"title": "Code", "done": True}]
