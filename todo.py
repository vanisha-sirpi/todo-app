tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Available Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
