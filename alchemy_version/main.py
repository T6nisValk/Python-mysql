import crud

# Make it an actual todo app
if __name__ == "__main__":
    list_name = input("Enter the name of the list: ")
    crud.create_todo_list(list_name)

    task_title = input("Task title: ")
    crud.create_task(1, task_title)

    tasks = crud.select_tasks()
    print(tasks[0].item_id)
    one_task = crud.select_task(tasks[0].item_id)
    crud.make_complete(one_task.item_id)
    print(one_task.name)
    if one_task.state:
        print("Completed.")
    else:
        print("Not completed.")

    crud.delete_task(one_task.item_id)
