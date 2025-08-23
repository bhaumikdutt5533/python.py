 import random

print(" Welcome to Number Guessing Game ")

# computer picks a random number between 1 and 10
number = random.randint(1, 10)

# ask the player to guess
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed it right!")
else:
    print(f" Oops! The correct number was {number}")