#blackjack game
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
comp_hand = []

def draw_cards():
    user_hand = random.sample(cards, 2)
    comp_hand = random.sample(cards, 2)
    return user_hand, comp_hand
    
should_cont = True
#play = input("Do you want to play a game of blackjack? Type 'y' or 'n' :")
draw_cards()
#if play == "y":
    


print(user_hand)