# Create a program that prompts the user to input their name once.
# Then, the program prints out the name once with the first letter capitalized.

prompt = input("What is your name: ")

print(f"Your name is {prompt.title()}")