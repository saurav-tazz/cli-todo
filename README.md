# CLI To-Do App

A small command-line to-do list written in Python. It is my first project built from scratch while learning Python and backend development.

## Features

- Add a task (the title is trimmed, cannot be empty, maximum 200 characters)
- View all tasks with a done / not done marker
- Menu input is validated, so typing a letter or an out-of-range number does not crash the program

**In progress:** mark a task as done, delete a task, save tasks to a file.

## Requirements

- Python 3.12 or newer
- No external packages

## How to run

```powershell
git clone [<your-repo-url>](https://github.com/saurav-tazz/cli-todo)
cd cli-todo
python main.py
```

Optional: use a virtual environment. This project has no dependencies yet, so it is not required.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1      # macOS / Linux: source .venv/bin/activate
python main.py
```

## Example

```
====================
CLI TODO APP
====================

Menu
1. Add
2. View
3. Quit
Enter option (1-3): 1
Enter new task: Buy milk

Task Added Successfully!!!

Menu
1. Add
2. View
3. Quit
Enter option (1-3): 2
ToDo List
1. [ ] Buy milk
```

## How it is built

- A task is a dictionary: `{"title": "Buy milk", "done": False}`. The whole list is a list of these dictionaries.
- `add_task` owns the validation rules and raises `ValueError` for a bad title. The menu catches the error and shows the message.
- Functions that decide things take their inputs as parameters, so they can be tested on their own.

## What I practised

- Functions, lists and dictionaries
- Input validation with `try/except` and `raise`
- Git: branches, merges, small commits with clear messages
