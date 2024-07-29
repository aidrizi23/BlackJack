import random
import os


def clear_console():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_to_play = True


def calculate_score(cards):
    score = sum(cards)
    if 1 in cards and score + 10 <= 21:
        score += 10
    return score


while want_to_play:
    clear_console()
    user_cards = []
    dealer_cards = []
    user_current_score = 0
    dealer_current_score = 0
    choice = input("Do you want to play a game of BlackJack? ").lower()
    while choice not in ['y', 'yes', 'n', 'no']:
        choice = input("Please enter a valid prompt for the choice: ").lower()
    if choice in ['y', 'yes']:
        for _ in range(2):
            user_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))
        user_current_score = calculate_score(user_cards)
        dealer_current_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_current_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        get_another = input("Type 'y' to get another card and 'n' to pass: ").lower()
        while get_another not in ['y', 'yes', 'n', 'no']:
            get_another = input("Please enter a valid prompt for the choice: ").lower()

        while get_another in ['y', 'yes']:
            user_cards.append(random.choice(cards))
            user_current_score = calculate_score(user_cards)
            if user_current_score < 21:
                print(f"Your cards: {user_cards}, current score: {user_current_score}")
                print(f"Dealer's first card: {dealer_cards[0]}")
                get_another = input("Type 'y' to get another card and 'n' to pass: ").lower()
                while get_another not in ['y', 'yes', 'n', 'no']:
                    get_another = input("Please enter a valid prompt for the choice: ").lower()
            elif user_current_score == 21:
                print(f"Your cards: {user_cards}, current score: {user_current_score}")
                print(f"Dealer's cards: {dealer_cards}, current score: {dealer_current_score}")
                print("Congratulations! You Win!")
                input()
                break
            else:
                print(f"Your cards: {user_cards}, current score: {user_current_score}")
                print(f"Dealer's cards: {dealer_cards}, current score: {dealer_current_score}")
                print("You Lost")
                input()
                break

        if get_another in ['n', 'no']:
            while dealer_current_score < 17:
                dealer_cards.append(random.choice(cards))
                dealer_current_score = calculate_score(dealer_cards)

            print(f"Your cards: {user_cards}, current score: {user_current_score}")
            print(f"Dealer's cards: {dealer_cards}, current score: {dealer_current_score}")

            if dealer_current_score == 21 or (dealer_current_score > user_current_score and dealer_current_score <= 21):
                print("You lose")
                input()
            elif dealer_current_score == user_current_score:
                print("Draw")
                input()
            elif dealer_current_score > 21 or user_current_score > dealer_current_score:
                print("You win")
                input()


    else:
        want_to_play = False
