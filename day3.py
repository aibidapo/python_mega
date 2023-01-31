# Using 'match' 'case' to make selection in our code

todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show' | 'display':
            for item in todos:
                print(f"{item.title()}")

        case 'exit':
            print("Exiting your todo list......" )
            break

        case _:
            print(f"You entered an unknown command")

print("Exited!")