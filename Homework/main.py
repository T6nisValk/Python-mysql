import crud

if __name__ == "__main__":
    print("Welcome to Todo App!")
    while True:
        print("What would you like to do?")
        print("1 - Create a todo list\n"
              "2 - Create a task for todo list\n"
              "3 - Display all lists\n"
              "4 - Display all tasks\n"
              "5 - Delete a list\n"
              "6 - Delete a task\n"
              "7 - Set task status to complete\n"
              "8 - Set task status to not complete\n"
              "9 - Exit app")
        main_input = input("Enter selection: ")
        try:
            if main_input == "9":
                exit()
            elif main_input == "1":
                print("-"*100)
                print("To create a list, you need a name for the list.")
                user_input_name = input("Enter name: ")
                crud.create_todo_list(user_input_name)
                print(f"Todo list '{user_input_name}' succesfully created.")
                print("-"*100)
            elif main_input == "2":
                print("-"*100)
                print("To create a task, you need to know the list id to which you want to create the task for and a name for the task.")
                user_input_id = int(input("Enter ID: "))
                user_input_name = input("Enter name: ")
                crud.create_task(user_input_id, user_input_name)
                print(
                    f"Task '{user_input_name}' for list '{crud.select_list(user_input_id).title}' succesfully created.")
                print("-"*100)
            elif main_input == "3":
                print("-"*100)
                print("All the currently available todo lists are:")
                lists = crud.select_lists()
                for list in lists:
                    print(f"ID: {list.list_id}, Name: {list.title}")
                print("-"*100)
            elif main_input == "4":
                print("-"*100)
                print("All the currently available tasks are:")
                tasks = crud.select_tasks()
                for task in tasks:
                    print(
                        f"ID: {task.item_id}, Name: {task.name}, State: {'Completed' if task.state else 'Not completed'}, List ID: {task.list_id}")
                print("-"*100)
            elif main_input == "5":
                print("-"*100)
                print("To delete a list, you need to know the ID of the list.")
                user_input_id = int(input("Enter ID: "))
                list = crud.select_list(user_input_id).title
                crud.delete_list(user_input_id)
                print(f"List '{list}' succesfully deleted.")
                print("-"*100)
            elif main_input == "6":
                print("-"*100)
                print("To delete a task, you need to know the task ID.")
                user_input_id = int(input("Enter ID: "))
                task = crud.select_task(user_input_id).name
                crud.delete_task(user_input_id)
                print(f"Task '{task}' succesfully deleted.")
                print("-"*100)
            elif main_input == "7":
                print("-"*100)
                print("To set a task as completed, you need to know the task ID.")
                user_input_id = int(input("Enter ID: "))
                task = crud.select_task(user_input_id).name
                crud.make_complete(user_input_id)
                print(f"Task '{task}' status set as 'Completed'")
                print("-"*100)
            elif main_input == "8":
                print("-"*100)
                print("To set a task as not completed, you need to know the task ID.")
                user_input_id = int(input("Enter ID: "))
                task = crud.select_task(user_input_id).name
                crud.make_not_complete(user_input_id)
                print(f"Task '{task}' status set as 'Not Completed'")
                print("-"*100)
            else:
                print("-"*100)
                print("Not a valid input.")
                print("-"*100)
        # I am not sure about this error handling, but it works.. Probably needs tweaking.
        except AttributeError:  # This is for wrong number input.
            print("-"*100)
            print("Not a valid Task ID / List ID.")
            print("-"*100)
        except ValueError:  # This is for letter input instead of number.
            print("-"*100)
            print("Not a valid Task ID / List ID.")
            print("-"*100)
