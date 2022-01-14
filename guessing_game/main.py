# GUESSING GAME
import random
# guess the number
def guess_number(number,guess):
    if guess > number: 
        print(f"Guess is greater!")
        return "m"
    elif guess < number:
        print("Guess is smaller")
        return "l"
    else:
        print("Guess is correct")
        return "c"

# generate random number to guess 

def generate_random_number():
    random_number = random.choice(range(1,99))
    return random_number


# check stage difficulty
def check_stage_difficulty_lives(stage):
    lives = 0
    if stage == 1:
        lives = 5 
        return lives
    elif stage == 2:
        lives = 10
        return lives    
    





def run_game():

    game_over = False 
    random_number = generate_random_number()
    while not game_over:

        stage_difficulty = int(input("Enter 1 for normal and 2 for high difficulty: "))
        total_lives = check_stage_difficulty_lives(stage_difficulty)

        if stage_difficulty == 1 or stage_difficulty == 2:
            while total_lives > 0:
                guessed_number = int(input("Enter a guess: "))
                comparision = guess_number(random_number,guessed_number)
                if comparision == "m" or comparision == "l":
                    total_lives -= 1
                    print(f"Remaining lives are {total_lives}")
                    if total_lives == 0:
                        print("GAME OVER")
                        game_over = True
                        
                elif comparision == "c":
                    print("You guessed correct")
                    total_lives = 0
                    game_over = True
                else:
                    print("Invalid, Try again")
        else:
            print("Invalid entry, try again")





run_game()









