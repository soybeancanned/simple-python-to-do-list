import time

tasks = ["Draw", "Buy groceries"]

orgInputList = ["Add a new task", "Delete a task", "Quit"]

def display_tasks():
    print("\nCurrent tasks:")
    for i in range(len(tasks)):
        print(i + 1, "--", tasks[i])
    print("\n")

def user_options(number):
    try:
        if inputlist[number - 1] == "Add a new task":
            usernote = input("What note would you like to add: ")
            tasks.append(usernote)
            print("Updated List:")
            display_tasks()
        elif inputlist[number - 1] == "Delete a task":
            display_tasks()
            user_delete_note = input("Which task would you like to delete (enter the task number): ")
            tasks.pop(int(user_delete_note) - 1)
            print("Updated List:")
            display_tasks()
        elif inputlist[number - 1] == "Quit":
            print("Goodbye!")
            return True
    except IndexError:
        print("\nInvalid input. Please enter a number")


print("Welcome to the to-do list app :)")
print("Let's see what needs to be done:")

time.sleep(1)

if not tasks:
    print("\nAll caught up!")
    print("\n")
else:
    display_tasks()

time.sleep(1)

while True:
    inputlist = ["Add a new task", "Delete a task", "Quit"]
    if tasks:
        inputlist = orgInputList
        for i in range(len(inputlist)):
            print(i + 1, inputlist[i])
    else:
        inputlist.pop(1)
        for i in range(len(inputlist)):
            print(i + 1, inputlist[i])
    user_input = input("What would you like to do (enter the option number): ")
    user_input = int(user_input)
    if user_options(user_input):
            break