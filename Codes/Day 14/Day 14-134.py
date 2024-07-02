# HIGHER LOWER GAME
from gamedata import data
import random 
import art
#random cleb 
def cleb():
    '''Selects random Account from list'''
    return random.choice(data)

#printable cleb
def celibrity(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return F"{name}, a {description} from {country},"

#compare function
def compare_account(guess, a_follower,b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b" 
    
#Game...

def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = cleb()
    account_b = cleb()
    
    while game_should_continue:
        account_a = account_b
        account_b = cleb() 

        while account_a == account_b:
            account_b = cleb()
            
        print(f"Compare A: {celibrity(account_a)}. ")
        print(art.vs)
        print(f"Against B: {celibrity(account_b)}. ")

        guess = input("Who has more followers. Type 'A' or 'B': " ).lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = compare_account(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You are right your current score is {score}")
        else:
            game_should_continue = False
            print(f"Your guess was incorrect. Your score is {score}")

game()