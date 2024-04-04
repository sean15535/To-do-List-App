from functions import greetings, add_list, completed_task, delete_task  
print("Welcome to To-do List App")

while True:
    greetings()
    choice = int(input(">>> "))
    if choice == 1:
        greetings()
    elif choice == 2:
        add_list()
    elif choice == 3:
        completed_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Closing the To-do List App.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
