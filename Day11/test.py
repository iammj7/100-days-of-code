import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# print(logo)
user_cards = []
computer_cards = []


def deal_card(cards):
    for i in range(2):
        card1 = random.choice(cards)
        card2 = random.choice(cards)
        card3 = random.choice(cards)
        card4 = random.choice(cards)
        user_cards.append(card1)
        user_cards.append(card2)
        computer_cards.append(card3)
        computer_cards.append(card4)
        return cards


def calculate_score(score):
    total_score = sum(score)
    blackjack = 1
    if cards[0] and 10 in score:
        total_score = 0
    if cards[0] in score and total_score > 21:
        for i in score:
            if i == cards[0]:
                
                score.remove[11]
                score.append[1]

    return total_score


deal_card(cards)
print(user_cards)
print(computer_cards)
print(calculate_score(user_cards))
print(calculate_score(computer_cards))
