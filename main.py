import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []

game_loop = True

def calculate_score(card):
    if len(card) == 2 and sum(card) == 21:
        return 0
    if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)
    return int(sum(card))

while game_loop:
    answer = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    if answer != 'y' and answer != 'n':
        print("Invalid Input")
        break
    game_loop = answer == 'y'

    if not game_loop:
        break
    else:
        print('\n' * 100)

    print(logo)
    print()

    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))

    print(f"    Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"    Computer's first card: {computer_hand[0]}")

    if calculate_score(player_hand) == 0:
        print("Win with a Blackjack 😎")
    else:
        while calculate_score(player_hand) < 21:
            command = input("Type 'y' to get another card, type 'n' to pass: ")
            if command == 'y':
                player_hand.append(random.choice(cards))
                print(f"    Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
                print(f"    Computer's first card: {computer_hand[0]}")

            else:
                break

        final_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        while computer_score < 17:
            computer_hand.append(random.choice(cards))
            computer_score = calculate_score(computer_hand)

        print(f"    Your final hand: {player_hand}, final score: {final_score}")
        print(f"    Computer's final hand: {computer_hand}, final score: {computer_score}")

        if final_score <= 21:
            if computer_score > 21:
                print("Opponent went over!. You win!")
            elif final_score == computer_score:
                print("It's a tie!")
            elif final_score > computer_score:
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You went over. You lose! 🤭")

    computer_hand = []
    player_hand = []
