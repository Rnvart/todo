HELP = """
help - print help for the program.  
add - add a task to the list.  
show - print all added tasks."""

tasks = []

run = True

while run:
    command = input("Enter command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added")
    else:
        print("Unknown command")
        break

print("Goodbye!")