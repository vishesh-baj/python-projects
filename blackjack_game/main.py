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

# check totals
def check_card(deck_1, deck_2):
    return max(deck_1,deck_2)

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
            user_total = sum(generated_deck_user)
            computer_total = sum(generated_deck_computer)œ
            print(f"Your Deck is {generated_deck_user}, computer has: {random.choice(generated_deck_computer)}")

            turn_over = False 
            while not turn_over:
                direction_1 = int(input("press 1 to draw card, press 2 to show: "))
                if direction_1 == 1:
                    new_card_user = draw_card()
                    new_card_computer = draw_card()
                    user_total += new_card_user
                    computer_total += new_card_computer

                    if user_total >= 21:
                        print("You loose, Your  score is more than 21!")
                        turn_over = True
                    else:
                        print(f"Your score is: {user_total}")
                
                elif direction_1 == 2:
                    if user_total > computer_total and user_total < 21:
                        print(f'You Win! Your Score: {user_total}, Computer Score: {computer_total}')
                        turn_over = True
                        game_over = True
                    else: 
                        print(f'You Loose! Your Score: {user_total}, Computer Score: {computer_total}')
                        turn_over = True
                        game_over = True
                
                else: 
                    print("Invalid Entry try Again!")
        elif direction == "q":
            print("Program Terminted!!")

            game_over = True
        else:
            print("Invalid Input!")


