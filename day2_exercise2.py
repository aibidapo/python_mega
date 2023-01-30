# Create a program that prompts the user to input their name once.
# Then, the program repeatedly prints out the name with the first letter capitalized.

# Note --> This code loops forever.

prompt = input("What is your name: ")

while True:
    print(prompt.capitalize())
