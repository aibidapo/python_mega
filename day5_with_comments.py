# Improving the "show" output and including a 'complete' option


todos = []  # Initialize an empty list called todos to store the to-do items

while True:  # Start a continuous loop that runs until the user enters the "exit" command

    user_action = input("Type add, show, edit, complete, or exit: ")  # Prompt the user to enter a command
    user_action = user_action.strip()                                 # Strip leading/trailing whitespace from the user's input

    match user_action:                                                # Use a match statement to check the user's input against each possible command
        case 'add':                                                   # If the user enters "add", execute the following block of code
            todo = input("Enter a todo: ")                            # Prompt the user to enter a new to-do item
            todos.append(todo)                                        # Add the new item to the todos list using the append method

        case 'show' | 'display':                                      # If the user enters "show" or "display", execute the following block of code
            for index, item in enumerate(todos, 1):                   # Use the enumerate function to iterate over each item in the todos list
                print(f"{index}: {item.title()}")                     # Print each item with its corresponding index, using the title method to capitalize the first letter

        case 'edit':                                                  # If the user enters "edit", execute the following block of code
            number = int(input('Number of the todo to edit: '))       # Prompt the user to enter the number of the item to be edited
            number = number - 1                                       # Subtract 1 from the user's input to convert from 1-based indexing to 0-based indexing
            print(f"Item to edit is '{todos[number]}'?")              # Print a confirmation message with the current value of the selected item

            new_todo = input("Enter new todo: ")                      # Prompt the user to enter the new value for the item
            todos[number] = new_todo                                  # Replace the old value with the new value in the todos list

        case 'complete':                                              # If the user enters "complete", execute the following block of code
            number = int(input("Enter the number of the todo to complete: "))  # Prompt the user to enter the number of the item to be marked as completed
            completed = todos.pop(number -1)                          # Remove the completed item from the todos list using the pop method, and store its value in a variable
            print(f"You have completed {completed}")                  # Print a message indicating that the item has been completed

        case 'exit':                                                  # If the user enters "exit", execute the following block of code
            print("Exiting your todo list......" )                    # Print a message indicating that the program is exiting
            break                                                     # Exit the loop using the break keyword

        case _:                                                       # If the user enters any other command, execute the following block of code
            print(f"You entered an unknown command")                  # Print a message indicating that the command was unknown
