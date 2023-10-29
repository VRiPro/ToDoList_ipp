"""This script is used to test actions on a task list."""

from todoproject.task import TaskList

def main():
    """
    Simulate scenarios and ensure the code works correctly.

    This function creates a TaskList and performs various actions on it,
    such as adding tasks, completing tasks, and displaying the tasks.

    Args:
        None

    Returns:
        None
    """
    task_list = TaskList()
    # task_list.display_tasks()
    # ADDING 2 TASKS.
    task_list.add_task("Aller au BeForum", "Atelier negociation")
    task_list.add_task("Aller a Télécom", "TP Hadoop",
                       "critical", "2023-10-31")
    # task_list.display_tasks()
    # COMPLETING A TASK.
    task_list.complete_task(1)
    task_list.complete_task(1)
    # task_list.display_tasks()
    # REMOVING A TASK.
    task_list.remove_task(1)
    # DISPLAYING THE TASKS.
    task_list.display_tasks()

if __name__ == "__main__":
    main()