tasks = []

print("Welcome to Task Tracker")

while True:
    print("\nCommands: add | view | complete | exit")
    command = input("Enter command: ").strip().lower()

    if command == "add":
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            print("Task added.")
        else:
            print("Task cannot be empty.")

    elif command == "view":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif command == "complete":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number: ").strip())

                if num < 1 or num > len(tasks):
                    print("Invalid task number.")
                else:
                    tasks[num - 1] = "[x] " + tasks[num - 1]
                    print("Task completed.")

            except ValueError:
                print("Please enter a valid number.")

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid command.")
