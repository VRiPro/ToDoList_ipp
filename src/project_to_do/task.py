from datetime import datetime


class Task:
    def __init__(self, task_id, name, description):
        """_summary_

        Args:
            task_id (_type_): _description_
            name (_type_): _description_
            description (_type_): _description_
            date (_type_): _description_
            state (_type_): _description_
            category (_type_): _description_
            priority (_type_): _description_
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.modif_date = datetime.now()
        self.completed = False
        self.category = ""
        self.priority = ""
        # shall we add deadline ?

    def complete(self):
        """Set the task to completed
        """
        self.completed = True

    def update(self, name, description):
        """_summary_

        Args:
            name (_type_): _description_
            description (_type_): _description_
        """
        self.name = name
        self.description = description
        self.modif_date = datetime.now()


class CriticalTask(Task):
    def __init__(self, task_id, name, description, deadline):
        """_summary_

        Args:
            task_id (_type_): _description_
            name (_type_): _description_
            description (_type_): _description_
            date (_type_): _description_
            state (_type_): _description_
            category (_type_): _description_
            priority (_type_): _description_
        """
        super().__init__(task_id, name, description)
        self.priority = "Critical"
        self._CriticalTask__deadline = datetime.strptime(deadline, "%Y-%m-%d")

    @property
    def deadline(self):
        return self._CriticalTask__deadline
    
    @deadline.setter
    def deadline(self, deadline):
        """Setter of the deadline attribute
        """
        if isinstance(deadline, datetime):
            self._CriticalTask__deadline = deadline
        else:
            self._CriticalTask__deadline = datetime.strptime(deadline, "%Y-%m-%d")

    

class TaskList:
    def __init__(self):
        """_summary_
        """
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, name, description):
        """ Add a task in the list of tasks
            Update of the next task id

        Args:
            name (_type_): _description_
            description (_type_): _description_
        """
        task = Task(self.task_id_counter, name, description)
        self.tasks.append(task)
        self.task_id_counter += 1

    def complete_task(self, name):
        """_summary_
        Complete the first task with the name=="name"
        Shall we select with the id if more than one have the same name ?
        Args:
            name (_type_): _description_
        """
        for task in self.tasks:
            if task.name == name:
                task.complete()
                break

    def remove_task(self, name):
        """_summary_
        Remove the first task with the name=="name"
        Shall we select with the id if more than one have the same name ?
        Args:
            name (_type_): _description_
        """
        task_to_remove = None
        for task in self.tasks:
            if task.name == name:
                task_to_remove = task
                break

        self.tasks.remove(task_to_remove)

    def display_tasks(self):
        """ Display task if the list is not empty
            Else disply no task

        """
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
