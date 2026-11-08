# CLI To-Do App

A small command-line to-do list written in Python. It is my first project built from scratch while learning Python and backend development.

## Features

- Add a task (the title is trimmed, cannot be empty, maximum 200 characters)
- View all tasks with a done / not done marker
- Mark a task as done. If the list is empty, a message is shown and the program returns to the menu
- Delete a task. Like marking, it shows a message and returns to the menu if the list is empty
- Menu input is validated, so typing a letter or an out-of-range number does not crash the program
- Tasks are saved to `tasks.json` after every change and loaded when the app starts
- If `tasks.json` is damaged, the program prints a message and exits without changing the file

## Requirements

- Python 3.12 or newer
- No external packages

## How to run

```powershell
git clone https://github.com/saurav-tazz/cli-todo.git
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
3. Mark
4. Delete
5. Quit
Enter option (1-5): 1
Enter new task: Build a CLI To-Do App

Task Added Successfully!!!


Menu
1. Add
2. View
3. Mark
4. Delete
5. Quit
Enter option (1-5): 2
ToDo List
1. [ ] Build a CLI To-Do App

Menu
1. Add
2. View
3. Mark
4. Delete
5. Quit
Enter option (1-5): 3
ToDo List
1. [ ] Build a CLI To-Do App
Enter the task you want to mark (1): 1

Marked Task Done!!!

Menu
1. Add
2. View
3. Mark
4. Delete
5. Quit
Enter option (1-5): 4
ToDo List
1. [x] Build a CLI To-Do App
Enter the task you want to delete (1): 1

Deleted Task!!!

Menu
1. Add
2. View
3. Mark
4. Delete
5. Quit
Enter option (1-5): 2
Sorry your ToDo list is empty.
```

## How it is built

- A task is a dictionary: `{"title": "Buy milk", "done": False}`. The whole list is a list of these dictionaries.
- `add_task`, `mark_task` and `delete_task` own their validation rules and raise `ValueError` for bad input. The menu catches the error and shows the message.
- Functions that decide things take their inputs as parameters, so they can be tested on their own.
- Tasks are saved as JSON after every successful change, so closing the program loses nothing.
- If the file is damaged, the program quits before the menu, so a save can never overwrite the broken file.

## What I practised

- Functions, lists and dictionaries
- Input validation with `try/except` and `raise`
- Saving and loading data with JSON files
- Git: branches, merges, small commits with clear messages

## Improvements

- `save_tasks` can still fail with an error that is not a `ValueError`, for example if the file is read-only (`PermissionError`).
- Ask the user for a filename if they want to use a personal file.