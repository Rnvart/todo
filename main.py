import random

HELP = """
help - print help for the program.  
add - add a task to the list.  
show - print all added tasks.
random - add a random task for the date Today"""

RANDOM_TASKS = ["Sign up for a course", "Write a letter to Guido", "Feed the cat", "Wash the car"]

tasks = {

}

# Today, Tomorrow, 31.12 ...
# [Task1, Task2, Task3]
# Date -> [Task1, Task2, Task3]

run = True

def add_todo(date, task):
    if date in tasks:
        # The date is in the dictionary
        # Add a task to the list
        tasks[date].append(task)
    else:
        # No date in dictionary
        # Create an entry with key date
        tasks[date] = []
        tasks[date].append(task)
    print("Task ", task, " added on date ", date)

while run:
    command = input("Enter command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Enter a date to display the list of tasks: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("No such date")
    elif command == "add":
        date = input("Enter a date to add a task: ")
        task = input("Enter task name: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Today", task)
    else:
        print("Unknown command")
        break

print("Goodbye!")