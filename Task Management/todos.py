
# Task Management System
def task():
    tasks = [] # Empty list to store tasks
    print("Welcome to the Task Manager!")

    total_task = int(input("Enter, how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task = input(f"Enter the task {i}: ")
        tasks.append(task)

    print(f"Todays tasks are:\n {tasks}")

    while True:
        operation = int(input("Enter 1 to add a task \n 2 to Update task \n 3 to delete a task \n 4 to view all tasks \n 5 to exit:\n "))
        if operation == 1:
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            print(f"task {new_task} added successfully!")

        elif operation == 2:
            old_task = input("Enter the task you want to update: ")
            if old_task in tasks:
                index = tasks.index(old_task)
                new_task = input("Enter the new task: ")
                tasks[index] = new_task
                print(f"task {old_task} updated to {new_task} successfully!")
            else:
                print("Task not found!")

        elif operation == 3:
            task = input("Enter the task you want to delete: ")
            if task in tasks:
                tasks.remove(task)
                print(f"task {task} deleted successfully!")

            else:
                print("Task not found!")

        elif operation == 4:
            print(f"Your tasks are:\n {tasks}")

        elif operation == 5:
            print("Thank you for using the Task Manager!")
            break
        
        else:
            print("Invalid input! Please try again.")

task() 