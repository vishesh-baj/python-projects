# BLACK JACK GAME 
import random


# ask user name 

def ask_user_name():
    user_name = input("Enter username: ")
    return user_name

# draw random two cards from deck 

def draw_card():
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(deck)

# run game 
def run_game():
    game_over = False 

    while not game_over:
        user_name = ask_user_name()
        print(f"Hi! {user_name}, Do you wanna play black jack?: ")
        direction = input("Press 'y' to play, press 'q' to leave the table: ")

        if direction == "y":
            generated_deck_user = [draw_card(),draw_card()]
            generated_deck_computer = [draw_card(),draw_card()]
            

        elif direction == "q":
            print("Program Terminted!!")
            game_over = True
        else:
            print("Invalid Input!")



run_game()
