todo_list = []
def greetings():
    print("\nWhat are your plans for today?")
    print("1. Display To-Do List\n2. Add Task\n3. Mark Task as Completed\n4. Remove Task\n5. Exit")

def display_list():
    if not todo_list:
        print("Your To-do list is empty")
        return
    print("Your To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
def add_list():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added to your to-do list.")
