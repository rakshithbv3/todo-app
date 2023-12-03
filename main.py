import functions

while True:
    user_action = input("Type add, show, edit , complete or exit :")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todo()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todo("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1} - {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todo()

            new_todo = input("Enter the new todo to replace: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Enter the valid command")\

            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todo()
            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"

            print(message)
        except (ValueError, IndexError):
            print("Enter a valid command")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Type a valid input")
print("Bye")
