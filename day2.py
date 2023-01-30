user_prompt = "Enter a 'todo: "

response = True

tasks = []

while response != 'done':

    response = input(user_prompt)

# Adding to prevent 'done' from being added to the list of todos

    if response == 'done':
        continue

    tasks.append(response.capitalize())

    print("Next item....")


print(f'Your todo list is: {tasks}')
