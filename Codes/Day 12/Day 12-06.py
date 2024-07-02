import random
import logo 
lvl_easy = 10
lvl_hard = 5
answer = random.randint(1, 100)
print(f"pssttt the num is {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return lvl_easy
    elif level == "hard":
        return lvl_hard 

def check_guess(guess, answer , turns):
    if guess == answer:
        print(f"You got it. Your number is {answer} ") 
    elif guess > answer:
        print(f"Too high.")
        return turns - 1
    elif guess < answer:
        print(f"Too low")
        return turns - 1
def game():

    print(logo.logo)
    print("Welcome to Guess the Number game. ")
    print("Am thinking of a number between 1 to 100. ")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining attempts to win the game. ")
        guess = int(input("Make a guess: "))
        
        turns = check_guess(guess , answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()