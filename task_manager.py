# Task Manager Application

def add_task():
    task = input("Enter new task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added!\n")


def view_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks found.\n")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
                print()
    except FileNotFoundError:
        print("No file found.\n")


def delete_task():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()

        view_tasks()
        num = int(input("Enter task number to delete: "))
        
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)

            with open("tasks.txt", "w") as f:
                f.writelines(tasks)

            print("Task deleted!\n")
        else:
            print("Invalid number!\n")

    except:
        print("Error occurred!\n")


def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()
