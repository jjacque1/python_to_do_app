import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(todolist, file)


def next_id():
    if len(todolist) == 0:
        return 1
    ids = [task["id"] for task in todolist]
    return max(ids) + 1


def main_menu():
    menu_items = [
        "Add task",
        "View tasks",
        "Clear list",
        "Delete task",
        "Mark complete",
        "Mark incomplete",
        "Exit",
    ]
    for number, items in enumerate(menu_items, start=1):
        print("{}.{} ".format(number, items))


def add_task():
    title = input("What task do you want to add? ")
    answer = input("Is the task done? (yes/no) ")
    done = answer.strip().lower() == "yes"
    task = {"title": title, "done": done, "id": next_id()}
    todolist.append(task)
    save_tasks()
    print("{} has been added successfully. ".format(task["title"]))
    view_tasks()


def view_tasks():
    if len(todolist) == 0:
        print("You have no tasks on your todo list.")
    for task in todolist:
        if task["done"]:
            status = "[x]"

        else:
            status = "[ ]"
        print("{}. {} {}".format(task["id"], status, task["title"]))


def set_done(value):

    if len(todolist) == 0:
        print("No tasks in list, add task to edit.")
        return

    if value:
        label = "complete"
    else:
        label = "incomplete"

    user_input = input("What task do you want to mark as {}? ".format(label))

    try:

        number = int(user_input)

        for task in todolist:
            if task["id"] == number:
                if task["done"] == value:
                    print("Task id #{} is already {}.".format(task["id"], label))
                    return
                else:
                    task["done"] = value
                    save_tasks()
                    print("Task #{} is marked as {}.".format(task["id"], label))
                    return
        print("Task ID #{} not found.".format(number))

    except ValueError:

        for task in todolist:
            if task["title"].lower() == user_input.lower():
                if task["done"] == value:
                    print(
                        "Task title '{}'  is already {}.".format(task["title"], label)
                    )
                    return
                else:
                    task["done"] = value
                    save_tasks()
                    print(
                        "Task title '{}' is marked as {}.".format(task["title"], label)
                    )
                    return
        print("Task title '{}' not found.".format(user_input))


def delete_task():
    user_input = input("Enter a task name or number you want to delete. ")

    try:
        number = int(user_input)
        for task in todolist:
            if task["id"] == number:
                todolist.remove(task)
                save_tasks()
                print("{} was removed successfully.".format(task["title"]))
                return
        print("No task has ID {}.".format(number))
    except ValueError:
        for task in todolist:
            if task["title"].lower() == user_input.lower():
                todolist.remove(task)
                save_tasks()
                print("{} was removed successfully.".format(task["title"]))
                return
        print("No task has title {}.".format(user_input))


def clear_list():
    confirm = input("Are you sure you want to clear you task list? ")
    if confirm == "yes":
        todolist.clear()
        save_tasks()
        print("your list is now empty.")
        print(todolist)
    elif confirm == "no":
        print("back to main menu")
    else:
        print("invalid option. ")


todolist = load_tasks()

while True:
    print("Main Menu: ")
    main_menu()
    choice = input("What do you want to do? ")
    if choice == "Add task":
        add_task()
    elif choice == "View tasks":
        view_tasks()
    elif choice == "Mark complete":
        set_done(value=True)
    elif choice == "Mark incomplete":
        set_done(value=False)
    elif choice == "Clear list":
        clear_list()
    elif choice == "Delete task":
        delete_task()
    elif choice == "Exit":
        save_tasks()
        print("Good bye!")
        break
    else:
        print("{} is not an option, please select a valid choice. ".format(choice))
