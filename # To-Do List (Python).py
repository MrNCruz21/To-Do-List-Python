# To-Do List (Python)


tasks = []

def menu_show():
    print("\n--- To-Do List ---") 
    print("1 = Add a Task")
    print("2 = View Task")
    print("3 = Mark as Done")
    print("5 = Exit")

def task_add():
    task = input("Enter New Task: ")
    tasks.append({"task":task, "done":False})
    print(f"Task---'{task}'---is added!")

def task_view():
    if not tasks:
        print("No Tasks Yet!!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} [{status}]")

def marked_done(): 
    task_view()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as Done!!")
        else:
            print("Sorry, Invalid Number!")
    except ValueError: 
        print("Please Enter a Valid Number!")

def delete_task():
    task_view()
    if not tasks: 
        return
    try:
        index = int(input("Enter Task Number to Delete = ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Deleted task is -- {deleted['task']}")
        else:
            print("Invalid Number!!")  
    except ValueError:
        print("Please Enter a Valid Number!")

while True:
    print("\n")
    menu_show()
    choice = input("Choose An Option (1 to 5) -- ")

    if choice == '1':
        task_add()
    elif choice == '2':
        task_view()
    elif choice == '3':
        marked_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Good bye!!")
        break
    else: 
        print("Invalid Choice. Try again!")
    





