todo_list = []
print("Welcome to To-do List App")

while True:
    print("\nWhat are your plans for today?")
    print("1. Display To-Do List\n2. Add Task\n3. Mark Task as Completed\n4. Remove Task\n5. Exit")
    choice = input(">>> ")

    # Input Validation
    if not choice.isdigit():
        print("Invalid input. Please enter a numeric choice.")
        continue

    choice = int(choice)

    if choice == 1:
        if not todo_list:
            print("Your To-do list is empty")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    elif choice == 2:
        task = input("Enter the task you want to add: ")
        todo_list.append(task)
        print(f"Task '{task}' has been added to your to-do list.")

    elif choice == 3:
        if not todo_list:
            print("Your To-do list is empty")
        else:
            completed_task = None
            while True:
                try:
                    index = int(input("Enter the completed task number: "))
                    if 1 <= index <= len(todo_list):
                        completed_task = todo_list.pop(index - 1)
                        print(f"Task '{completed_task}' marked as completed.")
                        break
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a numeric task number.")

    elif choice == 4:
        if not todo_list:
            print("Your To-do list is empty")
        else:
            removed_task = None
            while True:
                try:
                    index = int(input("Enter the task number to remove: "))
                    if 1 <= index <= len(todo_list):
                        removed_task = todo_list.pop(index - 1)
                        print(f"Task '{removed_task}' removed from your to-do list.")
                        break
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a numeric task number.")

    elif choice == 5:
        print("Closing the To-do List App.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")