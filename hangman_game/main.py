# HANGMAN GAME 
import random
import random_words
import hangman_pics

# ask user its name
def ask_user_input():
    user_name =  input("Enter your name: ")
    return user_name

# generate random word 
def generate_random_word():
    random_word = random.choice(random_words.words)
    return random_word

# ask user guess 
def ask_user_guess():
    user_guess = input("Enter your guess: ")
    return user_guess

# run the game 

def run_game():
    user_life = 7
    user_score = 0
    game_over = False

    while game_over == False:
        



