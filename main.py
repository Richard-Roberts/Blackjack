from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play():
    go = input("would you like to play black jack? Type \"Yes\" or \"No\" ").lower()
    if go == "yes":
        deal()
    else:
        "Too bad"


def deal():
    your_cards = [random.choice(cards), random.choice(cards)]
    print(f"Your cards: {your_cards}")
    computer_cards = [random.choice(cards), random.choice(cards)]
    print(f"Computer's first cards: {computer_cards[0]}")
    if sum(your_cards) == 21:
        print(f" Your cards: {your_cards} Blackjack! You win!")
        return
    another = input("Type \"y\" to get another card, type \"n\" to pass. ")
    if another == "y":
        hit = True
    else:
        hit = False
    while hit:
        your_cards.append(random.choice(cards))
        while 11 in your_cards and sum(your_cards) > 21:
            your_cards.remove(11)
            your_cards.append(1)
        print(f"Your cards: {your_cards}")
        if sum(your_cards) > 21:
            print("Bust!")
            again = input("Want to play again? Type \"Yes\" or \"No\" ").lower()
            if again == "yes":
                deal()
            else:
                return
        if sum(your_cards) == 21:
            print(f" Your cards: {your_cards} Blackjack! You win!")
            return
        another = input("Type \"y\" to get another card, type \"n\" to pass. ")
        if another == "n":
            hit = False
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        while 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards.remove(11)
            computer_cards.append(1)
    if sum(computer_cards) > 21:
        print(f"{computer_cards}")
        print("Dealer Busts! You Win")
        return
    print(f"Computers cards = {computer_cards}")
    if sum(computer_cards) > sum(your_cards):
        print("Computer Wins!")
    else:
        print("You Win!")
    play()


play()
