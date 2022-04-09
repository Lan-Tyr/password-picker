import random
import string

adjectives = ["hyper", "scratchy", "sleepy", "slow", "smelly", "wet", "fat", "red", "orange", "yellow", "green", "blue", "purple", "fluffy", "white", "proud", "brave"]
nouns = ["apple", "dinosaur", "ball", "toastre", "goat", "dragon", "hammer", "duck", "panda", "teacher", "peanut", "monkey", "llama", "soup"]
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

print("Welcome to Password Picker!")

while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        colour = random.choice(colours)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + colour + noun + str(number) + special_char
        print("Your new password is: %s" % password)

    response = input("Would you like another password? Type y or n: ")
    if response == "n":
        break