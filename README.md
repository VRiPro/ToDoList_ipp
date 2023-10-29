# ToDo List
This repo contains code for our "Kit Big Data" class project at Télécom Paris (2023-2024)

To decide on which python version we will be using [This website](https://devguide.python.org/versions/) as a reference

## Project Description:
A python library for personal tasks management.

## How to setup ?
1 - Clone the repository on your computer to get the code for the first time. If already done, you can just pull the updated version.

2 - It's preferable to have `python 3.9` installed on your computer.

3 - If you don't have poetry installed type:
```sh
pip install poetry
```

4 - If you have `python 3.9` create a virtual environment using it:
* to make our environment's path in your project folder, run this command
```sh
poetry config virtualenvs.in-project true 
```
* to create the virtual env run this command :
```sh
poetry env use 3.9 
```
* then activate the virtual environment with this command :
```sh
poetry shell      
```

5 - Some useful commands for poetry in virtual environment : 
* To add a dependency
```sh
poetry add package-name      
```
* To remove a dependency
```sh
poetry remove package-name      
```
* To install added dependencies
```sh
poetry install     
```

## Testing

### Test Cases

| Test Case Description     | Input                                     | Expected Output                                |
|---------------------------|-------------------------------------------|------------------------------------------------|
| Task Init Test            | Task(1, "Test", "Read a book")            | Initialized Task object with the expected attributes and data types.  |
| Task Complete Test        | Task(1, "Test", "Read a book")            | 'completed' attribute set to `True` after calling    `complete` method.|
| Task Update Test          |`Task(1, "Test", "Read a book")`           | 'name' and 'description' attributes updated to new values.|
| TaskList Init Test        |`TaskList()`                               | Initialized TaskList object with an empty 'tasks' list and 'task_id_counter' set to 1.  |
| TaskList Add Task Test    |`TaskList()`, `add_task("Test Task", "Read a book")` | Task added to 'tasks' list, and 'task_id_counter' incremented by 1.  |
| TaskList Complete Task Test| `TaskList()` with tasks, `complete_task("Task1")`|First task in 'tasks' marked as completed (attribute 'completed' set to `True`).  |
| TaskList Remove Task Test  | `TaskList()` with tasks, `remove_task("Task1")` |First task in 'tasks' is removed.  |
