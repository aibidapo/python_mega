# user_prompt = input("Enter a 'todo: ")

response = True

tasks = []

while response != 'done':

    response = input("Enter a 'todo: ")

# Adding to prevent 'done' from being added to the list of todos

    if response == 'done':
        continue

    tasks.append(response)

    print("Next item....")


print(f'Your todo list is: {tasks}')
