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


def main_menu():
    menu_items = [
        "Add task",
        "View tasks",
        "Clear task list",
        "Delete a task",
        "Mark done",
        "Exit",
    ]
    for number, items in enumerate(menu_items, start=1):
        print("{}.{} ".format(number, items))


def add_task():
    title = input("What task do you want to add? ")
    answer = input("Is the task done? (yes/no) ")
    done = answer.strip().lower() == "yes"
    task = {"title": title, "done": done}
    todolist.append(task)
    print("{} has been added successfully. ".format(task["title"]))


def view_tasks():
    if len(todolist) == 0:
        print("You have no tasks on your todo list.")
    for number, task in enumerate(todolist, start=1):
        if task["done"]:
            status = "[x]"

        else:
            status = "[ ]"
        print("{}. {} {}".format(number, status, task["title"]))


def mark_done():
    if len(todolist) == 0:
        print("No items in list, add items to mark done.")
        return
    user_input = input("Which task do you want to mark as done? ")

    if user_input.isdigit():
        number = int(user_input)
        if number >= 1 and number <= len(todolist):
            task = todolist[number - 1]
            if task["done"] == False:
                task["done"] = True
                print("{} is marked as done.".format(user_input))
            else:
                print("{} is already done.".format(user_input))
        else:
            print("{} is not a valid task number.".format(user_input))
    else:
        for task in todolist:
            if task["title"] == user_input:
                if task["done"] == False:
                    task["done"] = True
                    print("{} is marked as done.".format(user_input))
                    return
                else:
                    print("Task is already done.")
                    return
        print("{} is not a valid task title.".format(user_input))


def delete_a_task():
    user_input = input("Input the task name or number that you want to delete. ")
    if user_input.isdigit():
        number = int(user_input)
        if number >= 1 and number <= len(todolist):
            removed = todolist.pop(number - 1)
            print("{} has been deleted.".format(removed["title"]))
        else:
            print("{} is not a valid task number".format(number))
    else:
        for task in todolist:
            if task["title"] == user_input:
                todolist.remove(task)
                print("{} has been deleted".format(user_input))
                return
        print("{} is not in your todo list.".format(user_input))


def clear_my_lists():
    confirm = input("Are you sure you want to clear you task list? ")
    if confirm == "yes":
        todolist.clear()
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
    elif choice == "Mark done":
        mark_done()
    elif choice == "Clear task list":
        clear_my_lists()
    elif choice == "Delete a task":
        delete_a_task()
    elif choice == "Exit":
        save_tasks()
        print("Good bye!")
        break
    else:
        print("{} is not an option, please select a valid choice. ".format(choice))
