from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("This is the time")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, remove or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):
        todos = get_todos('todos.txt')
        print("My Todo List:")

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter New Todo:")
            todos[number] = new_todo

            write_todos(todos, "todos.txt")

            print("Changes applied successfully:", new_todo.title())

        except ValueError:
            print("Enter Valid Number.")
        continue

    elif user_action.startswith("remove"):
        try:
            number = int(user_action[6:])
            print(number)

            todos = get_todos()

            todos.pop(number - 1)

            write_todos(todos, "todos.txt")

            print("Item removed successfully")
        except IndexError:
            print("Enter Valid Index Number.")
        continue

    elif user_action.startswith("exit"):
        print("Thank you!!")
        break

    else:
        print("Please enter a valid command.")
