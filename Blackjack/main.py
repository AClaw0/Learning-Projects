import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_start_cards():
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    card3 = random.choice(cards)
    return card1, card2, card3

def end_game():
    global playing  # This is necessary for modifying the 'playing' variable outside the function
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {bot_cards}, final score: {bot_score}")
    if user_score == 21:
        print("You win with a Blackjack!")
    elif user_score > bot_score and not user_score > 21:
        print("You win!")
    elif bot_score > user_score and bot_score > 21:
        print("Opponent went over. You win!")
    else:
        print("You lose.")
    playing = False  # Set playing to False to exit the main game loop

def user_draw_card():
    card = random.choice(cards)
    user_cards.append(card)

def bot_draw_card():
    card = random.choice(cards)
    bot_cards.append(card)

# Main loop for restarting the game
while True:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == "y":
        playing = True
        # Initialize/reset card lists
        user_cards = []
        bot_cards = []
        while playing:
            print(logo)
            card1, card2, card3 = draw_start_cards()
            user_cards = [card1, card2]
            bot_cards = [card3]
            user_score = sum(user_cards)
            bot_score = sum(bot_cards)
            print(f"\tYour cards: {user_cards}, current score: {user_score}")
            print(f"\tComputer's first card: {bot_cards[0]}")
            if user_score == 21:
                end_game()  # Ends the game immediately if the user hits 21
                break
            else:
                while user_score < 21 and bot_score < 21:
                    draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if draw == "y":
                        user_draw_card()
                        user_score = sum(user_cards)
                        print(f"\tYour cards: {user_cards}, current score: {user_score}")
                        print(f"\tComputer's first card: {bot_cards[0]}")
                    elif draw == "n":
                        while bot_score < 21 and bot_score < user_score:
                            bot_draw_card()
                            bot_score = sum(bot_cards)
                        end_game()  # Ends the game after the bot finishes its turn
                        break
                    else:
                        print("Invalid Input")
                        break
    elif start == "n":
        print("Thanks for playing!")
        break  # Exit the loop if the user chooses not to play
    else:
        print("Invalid Input")
        continue  # Restart the loop if the input is invalid
