 #Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).   

import random
from socketserver import ThreadingUnixDatagramServer
# greeting and difficulty selection 
def choose_difficulty():
    print("Welcome to the Number Guessing Game! ")
    print("I am Thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
    return difficulty

# total attempts according to the difficulty level
def total_attempts(difficulty):
    if difficulty == "easy":
        print("You have choosen easy difficulty!")
        return 5
    elif difficulty == "hard":
        print("You have selected hard difficulty!")
        return 10

# number to be guessed
def return_guessing_number():
    guessing_number = random.choice(range(1,101))
    return guessing_number




# guess the number 
def guess_the_number(guessing_number):
    guess = int(input("make a guess: "))
    if guess == guessing_number:
        return True

    elif guess < guessing_number:
        print("Guess is too low")
        return False
    elif guess > guessing_number:
        print("Guess is too high")
        return False
    else:
        print("Invalid Number")

    




# run the game 

def run_game():
    difficulty = choose_difficulty()
    attempts = total_attempts(difficulty)
    guess_number = return_guessing_number()

    game_over = False 
    print(guess_number)
    while not game_over:
        if attempts > 0:
            if guess_the_number(guess_number) == True:
                print("Congratulations,You have guessed thge correct number")
                game_over = True
                attempts = 0
            elif guess_the_number(guess_number) == False:
                attempts -= 1
                print("You have entered a wrong guess")
                print(f"You have {attempts} left")
            else: 
                print("Something Happened! Game Terminated")
                game_over = False
                attempts = 0
        else:
            print("Game over! All lives are exhaused")
            game_over = True



run_game()
        



