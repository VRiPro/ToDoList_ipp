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


class TaskList:
    def __init__(self):
        """_summary_
        """
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, name, description):
        task = Task(self.task_id_counter, name, description)
        self.tasks.append(task)
        self.task_id_counter += 1

    def complete_task(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        for task in self.tasks:
            if task.name == name:
                task.complete()
                break

    def remove_task(self, name):
        """_summary_

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
        """ 
        """
        if len(self.tasks)==0 :
            print("No tasks")
        else :
            print("*********Tasks*********")
            print("ID\tNAME\tDESCRIPTION\tCOMPLETED")
            for task in self.tasks:
                print(f"{task.task_id}\t{task.name}\t{task.description}\t{task.completed}")
