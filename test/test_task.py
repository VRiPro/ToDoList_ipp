from src.project_to_do.task import Task, TaskList
from datetime import datetime

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
    assert task.completed == False
    assert task.category == ""
    assert task.priority == ""


def test_complete_task():
    """Test on the complete method
    """
    task = Task(1, "name", "description")
    task.complete()
    assert task.completed == True


def test_update_task():
    """Test on the update method
    """
    task = Task(1, "name", "description")
    task.update("new_name", "new_description")
    assert task.name == "new_name"
    assert task.description == "new_description"
    assert task.modif_date.date() == datetime.now().date()

# Unitary tests on the "taskList" class


def test_init_taskList():
    """Test on the initialization of the taskList
    """
    taskList = TaskList()
    assert taskList.tasks == []
    assert taskList.task_id_counter == 1


def test_add_task():
    """Test on the add_task method where only 1 task is added
    """
    taskList = TaskList()
    taskList.add_task("name", "description")
    assert taskList.tasks[0].task_id == 1
    assert taskList.tasks[0].name == "name"
    assert taskList.tasks[0].description == "description"
    assert taskList.tasks[0].date.date() == datetime.now().date()
    assert taskList.tasks[0].modif_date.date() == datetime.now().date()
    assert taskList.tasks[0].completed == False
    assert taskList.tasks[0].category == ""
    assert taskList.tasks[0].priority == ""
    assert len(taskList.tasks) == 1


def test_add_task2():
    """Test on the add_task method where 2 tasks are added
    """
    taskList = TaskList()
    taskList.add_task("name1", "description1")
    taskList.add_task("name2", "description2")
    assert taskList.tasks[1].task_id == 2
    assert taskList.tasks[1].name == "name2"
    assert taskList.tasks[1].description == "description2"
    assert len(taskList.tasks) == 2


def test_complete_task_in_TaskList():
    """Test on the complete_task method
    """
    taskList = TaskList()
    taskList.add_task("name", "description")
    taskList.complete_task("name")
    assert taskList.tasks[0].completed == True


def test_remove_task():
    """Test on the remove_task method with 1 task
    """
    taskList = TaskList()
    taskList.add_task("name", "description")
    taskList.remove_task("name")
    assert len(taskList.tasks) == 0


def test_display_no_tasks():
    """Test on the display_tasks method with no tasks
    """
    taskList = TaskList()
    assert taskList.display_tasks() == "No tasks"


def test_display_1_task():
    """Test on the display_tasks method with 1 task
    """
    taskList = TaskList()
    taskList.add_task("name", "description")
    assert taskList.display_tasks().strip() == ("*********Tasks*********\n"
                                                "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
                                                "1\tname\tdescription\tFalse").strip()


def test_display_2_tasks():
    """Test on the display_tasks method with 2 tasks
    """
    taskList = TaskList()
    taskList.add_task("name", "description")
    taskList.add_task("name2", "description2")
    assert taskList.display_tasks().strip() == ("*********Tasks*********\n"
                                                "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
                                                "1\tname\tdescription\tFalse\n"
                                                "2\tname2\tdescription2\tFalse").strip()


def test_display_1_task_complete():
    """Test on the display_tasks method with 1 task which is completed
    """
    taskList = TaskList()
    taskList.add_task("name", "description")
    taskList.complete_task("name")
    assert taskList.display_tasks().strip() == ("*********Tasks*********\n"
                                                "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
                                                "1\tname\tdescription\tTrue").strip()
