tasks  = []
def add_task():
    for i in range(50):
        print(".")
    new_task = input("Enter your new task: ")
    tasks.append(new_task)
    for i in range(50):
        print(".")
def del_task():
    for i in range(50):
        print(".")
    remove_task = input("Remove task: ")
    tasks.remove(remove_task)
    for i in range(50):
        print(".")
def view_tasks():
    for i in range(50):
        print(".")
    for i in range(len(tasks)):
        print(tasks[i])
    for i in range(3):
        print(".")
    
while True:
    print("1) Add task\n2) Remove task\n3) View tasks\n4) Exit")
    choice = int(input("Make a choice: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        del_task()
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        break
    else:
        print("Invalid input. Please try again")