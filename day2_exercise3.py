# Create a program that prompts the user to input their name repeatedly.
# Then, the program repeatedly prints out the name with the first letter capitalized.

# Note --> This code loops forever.

while True:
    prompt = input("What is your name: ")

    print(prompt.capitalize())
