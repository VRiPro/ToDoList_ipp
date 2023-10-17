from project_to_do.task import Task, TaskList

def main():
    task_list = TaskList()
    # task_list.display_tasks()

    task_list.add_task("Aller au BeForum" , "Atelier negociation")
    task_list.add_task("Aller a Télécom" , "TP Hadoop")
    # task_list.display_tasks()
    task_list.complete_task("Aller a Télécom")
    # task_list.display_tasks()
    task_list.remove_task("Aller a Télécom")
    task_list.display_tasks()

if __name__ == "__main__":
    main()   
    