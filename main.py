from functions import greetings, add_list
print("Welcome to To-do List App")

while True:
    greetings()
    choice = int(input(">>> "))

    if choice == 1:
        greetings()
    elif choice == 2:
        add_list()
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
