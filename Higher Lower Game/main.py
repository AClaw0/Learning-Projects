from art import logo,vs
from game_data import data
import random

game_active = True
score = 0

person_A = random.choice(data)
person_B = random.choice(data)

# Make sure the are no duplicates
while person_A == person_B:
    person_B = random.choice(data)

while game_active:
    print('\n' * 80)
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {person_A["name"]}, a {person_A["description"]}, from {person_A["country"]}.")
    print(vs)
    print(f"Against B: {person_B["name"]}, a {person_B["description"]}, from {person_B["country"]}.")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Determine correct answer
    if person_A["follower_count"] > person_B["follower_count"]:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

    if user_answer == correct_answer:
        score += 1
        if correct_answer == 'A':
            person_A = person_A
        else:
            person_A = person_B
        person_B = random.choice(data)
        while person_A == person_B:
            person_B = random.choice(data)
    else:
        game_active = False
        print(f"Sorry, that's wrong. Final score: {score}")
