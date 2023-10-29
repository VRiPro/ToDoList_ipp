"""This module provides the Task and TaskList classes for managing tasks.
"""
from datetime import datetime
from typing import List
from logger import debug_logger, error_logger


class Task:
    """Represents a task with attributes for identification,
    name, and description.

    This class provides methods to mark tasks as completed and
    update their name and description.

    Attributes:
        task_id (int): Unique identifier for the task.
        name (str): Name of the task.
        description (str): Description of the task.
        date (datetime): Date of task creation.
        modif_date (datetime): Date of the last modification.
        completed (bool): Indicates if the task is completed.
        category (str): Category of the task.
        priority (str): Priority level of the task.
    """

    def __init__(self, task_id: int, name: str, description: str):
        """Initialize a task.

        Args:
            task_id (int): Unique identifier for the task.
            name (str): Name of the task.
            description (str): Description of the task.
        """
        self.task_id: int = task_id
        self.name: str = name
        self.description: str = description
        self.date: datetime = datetime.now()
        self.modif_date: datetime = datetime.now()
        self.completed: bool = False
        self.category: str = ""
        self.priority: str = ""

    def complete(self) -> None:
        """Mark the task as completed."""
        if not self.completed:
            self.completed = True
            debug_logger.debug("Task %d completed", self.task_id)
        else:  # VR
            try:
                raise ErreursToDo(
                    "the task is already sets as completes !")  # vr
            except ErreursToDo as e:
                error_logger.error(e)

    def update(self, name: str, description: str) -> None:
        """Update the task's name and description.

        Args:
            name (str): New name for the task.
            description (str): New description for the task.
        """
        if self.name != name or self.description != description:  # vr
            self.name = name
            self.description = description
            self.modif_date = datetime.now()
            debug_logger.debug("Task %d updated successfully", self.task_id)
        else:  # vr
            try:
                raise ErreursToDo(
                    "Name and/or description were similar before update")  # vr
            except ErreursToDo as e:
                error_logger.error(e)



class CriticalTask(Task):
    """Represents a critical task that inherits from Task.

    This class extends the Task class with a 'Critical'
    priority level and a deadline attribute.


    Args:
        task_id (int): Unique identifier for the task.
        name (str): Name of the task.
        description (str): Description of the task.
        deadline (str or datetime): Deadline for the critical
                                    task (in the format "%Y-%m-%d"
                                    or as a datetime object).

    Attributes:
        deadline (datetime): Deadline for the critical task.

    Note:
        The 'deadline' attribute can be set as a string in
        "%Y-%m-%d" format or as a datetime object.
    """

    def __init__(self, task_id: int, name: str,
                 description: str, deadline: datetime) -> None:
        """Initialize a critical task with a
        'Critical' priority level and a deadline.

        Args:
            task_id (int): Unique identifier for the task.
            name (str): Name of the task.
            description (str): Description of the task.
            deadline (str or datetime): Deadline for the critical
                                        task (in the format "%Y-%m-%d"
                                        or as a datetime object).
        """
        super().__init__(task_id, name, description)
        self.priority: str = "Critical"
        self.deadline: datetime = datetime.strptime(deadline, "%Y-%m-%d")

    @property
    def deadline(self) -> datetime:
        """Getter for the deadline attribute."""
        return self._CriticalTask__deadline

    @deadline.setter
    def deadline(self, deadline) -> None:
        """Setter for the deadline attribute.

        Args:
            deadline (str or datetime): Deadline for the critical
            task (in the format "%Y-%m-%d" or as a datetime object).
        """
        if isinstance(deadline, datetime):
            self._CriticalTask__deadline = deadline
            debug_logger.debug("date changed")
        else:
            try:
                self._CriticalTask__deadline = datetime.strptime(
                    deadline, "%Y-%m-%d")
            except ValueError as e:
                error_logger.error(e)


class TaskList:
    """Manages a list of tasks with methods to add, complete, remove,
    and display tasks.

    Attributes:
        tasks (list): List of tasks.
        task_id_counter (int): Counter to track the next available task ID.
    """

    def __init__(self) -> None:
        """Initialize a task list."""
        self.tasks: List[Task] = []
        self.task_id_counter: int = 1

    def add_task(self, name: str, description: str , critical: bool = False, deadline: datetime = None) -> None:
        """Add a task to the list and update the task ID.

        Args:
            name (str): Name of the task.
            description (str): Description of the task.
            critical (bool) : If the task is critical or not
            deadline (datetime or str): Deadline for the task in the
        """
        if critical:
            task = CriticalTask(self.task_id_counter, name, description, deadline)
        else :
            task = Task(self.task_id_counter, name, description)
        if task not in self.tasks:
            self.tasks.append(task)
            self.task_id_counter += 1
            debug_logger.debug("Task %d added successfully", task.task_id)
        else:
            try:
                raise ErreursToDo(
                    "A task with similar name and description exist")
            except ErreursToDo as e:
                error_logger.error(e)

    def complete_task(self, task_id: int) -> None:
        """Mark the first task with the given name as completed.

        Args:
            task_id (int): Id of the task to complete.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.complete()
                break

    def remove_task(self, task_id: int) -> None:
        """Remove a task by its Id.

        Args:
            task_id (int): Id of the task to remove.
        """
        id_found: bool = False
        task_to_remove: Task = None
        for task in self.tasks:
            if task.task_id == task_id:
                id_found = True
                task_to_remove = task
                break
        debug_logger.debug("Task %d removed successfully", task_to_remove.task_id)
        try:
            if id_found:
                self.tasks.remove(task_to_remove)
            else:
                raise ErreursToDo("The ID of the task does not exist")  # vr
        except ErreursToDo as e:
            error_logger.error(e)

    def display_tasks(self) -> str:
        """Display tasks in the list, or indicate
        no tasks if the list is empty."""
        if len(self.tasks) == 0:
            print("No tasks")
            debug_logger.debug("No tasks")
            return "No tasks"
        else:
            result: str = "*********Tasks*********\n"
            result += "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
            print("*********Tasks*********")
            print("ID\tNAME\tDESCRIPTION\tCOMPLETED")
            for task in self.tasks:
                task_id: int = task.task_id
                name: str = task.name
                description: str = task.description
                completed: bool = task.completed
                task: str = f"{task_id}\t{name}\t{description}\t{completed}\n"
                result += task
                print(task)
                debug_logger.debug("Tasks are displayed")
            return result


class ErreursToDo(Exception):
    """A custom Exeption Type of our project
    """
    def __init__(self, message: str = "Une erreur est survenue") -> None:
        self.message: str = message
        super().__init__(self.message)
