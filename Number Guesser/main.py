import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid Input. Please restart the game.")
    exit()

number = random.randint(1, 100)
print(number)

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")
        exit()

    lives -= 1

    if lives == 0:
        print(f"You've run out of guesses. The correct number was {number}.")
        exit()

    if guess < number:
        print("Too low.")
        print("Guess again.")
    elif guess > number:
        print("Too high.")
        print("Guess again.")
    else:
        print("Invalid Input.")

print("You've run out of guesses. Refresh the page to run again.")
