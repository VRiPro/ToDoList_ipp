from datetime import datetime
from project_to_do.utils.logger import logger


class Task:
    """Represents a task with attributes for identification, name, and description.

    This class provides methods to mark tasks as completed and update their name and description.

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

    def __init__(self, task_id, name, description):
        """Initialize a task.

        Args:
            task_id (int): Unique identifier for the task.
            name (str): Name of the task.
            description (str): Description of the task.
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.modif_date = datetime.now()
        self.completed = False
        self.category = ""
        self.priority = ""

    def complete(self):
        """Mark the task as completed."""
        if self.completed != True:  # VR
            self.completed = True
        else:  # VR
            try:
                raise ErreursToDo(
                    "the task is already sets as completes !")  # vr
            except ErreursToDo as e:
                print(e)

    def update(self, name, description):
        """Update the task's name and description.

        Args:
            name (str): New name for the task.
            description (str): New description for the task.
        """
        if self.name != name or self.description != description:  # vr
            self.name = name
            self.description = description
            self.modif_date = datetime.now()
        else:  # vr
            try:
                raise ErreursToDo(
                    "Name and description were similar before update")  # vr
            except ErreursToDo as e:
                print(e)


class TaskList:
    """Manages a list of tasks with methods to add, complete, remove, and display tasks.

    Attributes:
        tasks (list): List of tasks.
        task_id_counter (int): Counter to track the next available task ID.
    """

    def __init__(self):
        """Initialize a task list."""
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, name, description):
        """Add a task to the list and update the task ID.

        Args:
            name (str): Name of the task.
            description (str): Description of the task.
        """
        task = Task(self.task_id_counter, name, description)
        if not task in self.tasks:
            self.tasks.append(task)
            self.task_id_counter += 1
            logger.debug(f"Task {task.task_id} added")
        else:
            try:
                raise ErreursToDo(
                    "A task with similar name and description exist")
            except ErreursToDo as e:
                print(e)

    def complete_task(self, name):
        """Mark the first task with the given name as completed.

        Args:
            name (str): Name of the task to complete.
        """
        for task in self.tasks:
            if task.name == name:
                task.complete()
                break

    def remove_task(self, task_id):
        """Remove a task by its ID.

        Args:
            task_id (int): ID of the task to remove.
        """
        id_found = False
        task_to_remove = None
        for task in self.tasks:
            if task.task_id == task_id:
                id_found = True
                task_to_remove = task
                break
        try:
            if id_found == True:
                self.tasks.remove(task_to_remove)
            else:
                raise ErreursToDo("The ID of the task does not exist")  # vr
        except ErreursToDo as e:
            print(e)

    def display_tasks(self):
        """Display tasks in the list, or indicate no tasks if the list is empty."""
        if len(self.tasks) == 0:
            print("No tasks")
            return "No tasks"
        else:
            result = "*********Tasks*********\n"
            result += "ID\tNAME\tDESCRIPTION\tCOMPLETED\n"
            print("*********Tasks*********")
            print("ID\tNAME\tDESCRIPTION\tCOMPLETED")
            for task in self.tasks:
                result += f"{task.task_id}\t{task.name}\t{task.description}\t{task.completed}\n"
                print(
                    f"{task.task_id}\t{task.name}\t{task.description}\t{task.completed}")
            return result


class CriticalTask(Task):
    """Represents a critical task that inherits from Task.

    This class extends the Task class with a 'Critical' priority level and a deadline attribute.

    Args:
        task_id (int): Unique identifier for the task.
        name (str): Name of the task.
        description (str): Description of the task.
        deadline (str or datetime): Deadline for the critical task (in the format "%Y-%m-%d" or as a datetime object).

    Attributes:
        deadline (datetime): Deadline for the critical task.

    Note:
        The 'deadline' attribute can be set as a string in "%Y-%m-%d" format or as a datetime object.
    """

    def __init__(self, task_id, name, description, deadline):
        """Initialize a critical task with a 'Critical' priority level and a deadline.

        Args:
            task_id (int): Unique identifier for the task.
            name (str): Name of the task.
            description (str): Description of the task.
            deadline (str or datetime): Deadline for the critical task (in the format "%Y-%m-%d" or as a datetime object).
        """
        super().__init__(task_id, name, description)
        self.priority = "Critical"
        self._CriticalTask__deadline = datetime.strptime(deadline, "%Y-%m-%d")

    @property
    def deadline(self):
        """Getter for the deadline attribute."""
        return self._CriticalTask__deadline

    @deadline.setter
    def deadline(self, deadline):
        """Setter for the deadline attribute.

        Args:
            deadline (str or datetime): Deadline for the critical task (in the format "%Y-%m-%d" or as a datetime object).
        """
        if isinstance(deadline, datetime):
            self._CriticalTask__deadline = deadline
        else:
            self._CriticalTask__deadline = datetime.strptime(
                deadline, "%Y-%m-%d")


class ErreursToDo(Exception):
    def __init__(self, message="Une erreur est survenue"):
        self.message = message
        super().__init__(self.message)
