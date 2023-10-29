"""This module tests the task.py module.
"""
from datetime import datetime
from todoproject.task import Task, CriticalTask, TaskList


# Unitary tests on the "task" class


def test_init_task():
    """Test on the initialization of the task
    """
    task = Task(1, "name", "description")
    assert task.task_id == 1
    assert task.name == "name"
    assert task.description == "description"
    assert task.date.date() == datetime.now().date()
    assert task.modif_date.date() == datetime.now().date()
    assert task.completed is False
    assert task.category == ""
    assert task.priority == ""


def test_complete_task():
    """Test on the complete method
    """
    task = Task(1, "name", "description")
    task.complete()
    assert task.completed is True


def test_update_task():
    """Test on the update method
    """
    task = Task(1, "name", "description")
    task.update("new_name", "new_description")
    assert task.name == "new_name"
    assert task.description == "new_description"
    assert task.modif_date.date() == datetime.now().date()

# Unitary tests on the "CriticalTask" class


def test_init_criticaltask():
    """Test on the initialization of the criticalTask
    """
    critical_task = CriticalTask(1, "ouloulou", "oulala", "2023-10-19")
    assert critical_task.task_id == 1
    assert critical_task.name == "ouloulou"
    assert critical_task.description == "oulala"
    assert critical_task._CriticalTask__deadline == datetime.strptime(
        "2023-10-19", "%Y-%m-%d")


def test_add_critical_task_with_deadline():
    """Test on adding a critical task with a deadline
    """
    task_list = TaskList()
    task_list.add_task("name", "description", 
                       critical=True, deadline="2023-10-19")
    assert isinstance(task_list.tasks[0], CriticalTask)
    assert task_list.tasks[0].deadline == datetime.strptime(
        "2023-10-19", "%Y-%m-%d")


def test_set_deadline():
    """Test on the setDeadline method
    """
    critical_task = CriticalTask(1, "ouloulou", "oulala", "2023-10-19")
    critical_task.deadline = datetime.strptime("2023-12-04", "%Y-%m-%d")
    assert critical_task.task_id == 1
    assert critical_task.name == "ouloulou"
    assert critical_task.description == "oulala"
    assert critical_task._CriticalTask__deadline == datetime.strptime(
        "2023-12-04", "%Y-%m-%d")

# Unitary tests on the "taskList" class


def test_init_task_list():
    """Test on the initialization of the taskList
    """
    task_list = TaskList()
    assert not task_list.tasks
    assert task_list.task_id_counter == 1


def test_add_task():
    """Test on the add_task method where only 1 task is added
    """
    task_list = TaskList()
    task_list.add_task("name", "description")
    assert task_list.tasks[0].task_id == 1
    assert task_list.tasks[0].name == "name"
    assert task_list.tasks[0].description == "description"
    assert task_list.tasks[0].date.date() == datetime.now().date()
    assert task_list.tasks[0].modif_date.date() == datetime.now().date()
    assert task_list.tasks[0].completed is False
    assert task_list.tasks[0].category == ""
    assert task_list.tasks[0].priority == ""
    assert len(task_list.tasks) == 1


def test_add_task2():
    """Test on the add_task method where 2 tasks are added
    """
    task_list = TaskList()
    task_list.add_task("name1", "description1")
    task_list.add_task("name2", "description2")
    assert task_list.tasks[1].task_id == 2
    assert task_list.tasks[1].name == "name2"
    assert task_list.tasks[1].description == "description2"
    assert len(task_list.tasks) == 2


def test_add_large_number_of_tasks():
    """Test adding a large number of tasks and check task IDs
    """
    task_list = TaskList()
    num_tasks = 100
    for i in range(1, num_tasks + 1):
        task_list.add_task(f"Task {i}", f"Description {i}")
    for i, task in enumerate(task_list.tasks, start=1):
        assert task.task_id == i

def test_complete_task_in_Task_list():
    """Test on the complete_task method
    """
    task_list = TaskList()
    task_list.add_task("name", "description")
    task_list.complete_task(1)
    assert task_list.tasks[0].completed is True


def test_remove_task():
    """Test on the remove_task method with 1 task
    """
    task_list = TaskList()
    task_list.add_task("name", "description")
    task_list.remove_task(1)
    assert len(task_list.tasks) == 0


def test_display_no_tasks(capfd):
    """Test on the display_tasks method with no tasks
    """
    task_list = TaskList()
    task_list.display_tasks()
    captured = capfd.readouterr()
    assert captured.out.strip() == "No tasks"


def test_display_1_task():
    """Test on the display_tasks method with 1 task
    """
    task_list = TaskList()
    task_list.add_task("name", "description")
    task_list.display_tasks()
    assert task_list.display_tasks().strip() == (
                            "*********Tasks*********\n"
                            "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
                            "1\tname\tdescription\tFalse").strip()


def test_display_2_tasks():
    """Test on the display_tasks method with 2 tasks
    """
    task_list = TaskList()
    task_list.add_task("name", "description")
    task_list.add_task("name2", "description2")

    assert task_list.display_tasks().strip() == (
                                    "*********Tasks*********\n"
                                    "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
                                    "1\tname\tdescription\tFalse\n"
                                    "2\tname2\tdescription2\tFalse").strip()


def test_display_1_task_complete():
    """Test on the display_tasks method with 1 task which is completed
    """
    task_list = TaskList()
    task_list.add_task("name", "description")
    task_list.complete_task(1)
    assert task_list.display_tasks().strip() == (
                                        "*********Tasks*********\n"
                                        "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
                                        "1\tname\tdescription\tTrue").strip()
