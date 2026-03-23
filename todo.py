#TASK1
tasks = []

def show_tasks():
    if not tasks:
        print("No Tasks Available.")
        return
    print("\n---Pending Tasks---")
    for i, task in enumerate(tasks):
        if not task["done"]:
            print(f"{i+1}. {task['title']}")
    print("\n---Completed Tasks---")
    for i, task in enumerate(tasks):
        if task["done"]:
            print(f"{i+1}. {task['title']}")

def add_task():
    while True:
        title = input("Enter task (or type 'q' to stop): ")
        if title.lower() in ["q", "quit", "stop"]:
            print("Stopped adding tasks.")
            break
        task = {"title": title, "done": False}
        tasks.append(task)
        print("Task added!")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num-1)
        print(f"Deleted: {removed['title']}")
    except:
        print("Invalid Input!")

def update_task():
    show_tasks()
    try:
        num = int(input("Enter task number to update: "))
        new_title = input("Enter new task: ")
        tasks[num-1]["title"] = new_title
        print("Task Updated!")
    except:
        print("Invalid input!")

def mark_complete():
    show_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num-1]["done"] = True
        print("Task marked as completed!")
    except:
        print("Invalid Input!")

# Main Loop
while True:
    print("\n======TO-DO LIST MENU======")
    print("1. View Tasks") 
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_complete()
    elif choice == '6':
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Try Again.")
