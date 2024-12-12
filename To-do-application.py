def displayTask(tasks):
    print("\n To-Do List:")
    if not tasks:
        print("No task avaliable")
    else:
        for i,task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        
    
def addTask(tasks):
    task = input("Enter a new task")
    tasks.append(task)
    print(f"Task {task} added in List successfully")
def removeTask(tasks):
    displayTask(tasks)
    try:
        tasks_num = int(input("Enter task Number"))
        if 1 <= tasks_num <= len(tasks):
            removed_task = tasks.pop(tasks_num - 1)
            print(f"{removed_task} task removed from List successfully")
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a valid number")
        
def main():
    tasks = []
    while True:
        print("To-Do App Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            displayTask(tasks)
        elif choice == '2':
            addTask(tasks)
        elif choice == '3':
            removeTask(tasks)
        elif choice == '4':
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
            
main()