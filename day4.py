# Enable the user to edit their entries

todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show' | 'display':
            for item in todos:
                print(f"{item.title()}")

        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            print(f"Item to edit is '{todos[number]}'?")

            new_todo = input("Enter new todo: ")

            todos[number] = new_todo

        case 'exit':
            print("Exiting your todo list......" )
            break

        case _:
            print(f"You entered an unknown command")

print("Exited!")