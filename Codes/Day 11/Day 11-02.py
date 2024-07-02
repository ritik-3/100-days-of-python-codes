import random
import art

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)  
def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw. -_- "
    elif comp_score == 0:
        return "Lose, Computer has Blackjack. :( "
    elif user_score == 0:
        return"Win with a Blackjack :-> "
    elif user_score > 21:
        return "You went over 21, you loose. :< "
    elif comp_score > 21:
        return "Opponent went over 21, You won. ;) "
    elif user_score > comp_score:
        return "you win, :) "
    else:
            "you loose :o "

def play_game():
    print(art.logo)
    
    is_game_over = False
    user_cards = []
    comp_cards = []
    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your card: {user_cards}, current score: {user_score} ")
        print(f"Computers first card: {comp_cards[0]}") 

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_shuld_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_shuld_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True
                
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score = calculate_score(comp_cards)

    print(compare(user_score, comp_cards))
while input("Do you wanna play a game of Blackjac? Type 'y' or 'n': ") == "y":
    play_game()