"""This module is used to try some actions on a task list.
"""
from todoproject.task import TaskList


def main():
    task_list = TaskList()
    # task_list.display_tasks()
    # AJOUT DE 2 TACHES.
    task_list.add_task("Aller au BeForum", "Atelier negociation")
    task_list.add_task("Aller a Télécom", "TP Hadoop",
                        "critical", "2023-10-31")
    # task_list.display_tasks()
    # ON COMPLETE UNE TACHE.
    task_list.complete_task(1)
    task_list.complete_task(1)
    # task_list.display_tasks()
    # ON SUPPRIME UNE TACHE.
    task_list.remove_task(1)
    # ON AFFICHE LES TACHES
    task_list.display_tasks()


if __name__ == "__main__":
    main()
