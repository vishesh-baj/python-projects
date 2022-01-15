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
    

# program to run ther game 
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




print(
    """
    
                                                                                                                                                          
  ,ad8888ba,                                                  88                                 ,ad8888ba,                                               
 d8"'    `"8b                                                 ""                                d8"'    `"8b                                              
d8'                                                                                            d8'                                                        
88             88       88   ,adPPYba,  ,adPPYba,  ,adPPYba,  88  8b,dPPYba,    ,adPPYb,d8     88             ,adPPYYba,  88,dPYba,,adPYba,    ,adPPYba,  
88      88888  88       88  a8P_____88  I8[    ""  I8[    ""  88  88P'   `"8a  a8"    `Y88     88      88888  ""     `Y8  88P'   "88"    "8a  a8P_____88  
Y8,        88  88       88  8PP"""""""   `"Y8ba,    `"Y8ba,   88  88       88  8b       88     Y8,        88  ,adPPPPP88  88      88      88  8PP"""""""  
 Y8a.    .a88  "8a,   ,a88  "8b,   ,aa  aa    ]8I  aa    ]8I  88  88       88  "8a,   ,d88      Y8a.    .a88  88,    ,88  88      88      88  "8b,   ,aa  
  `"Y88888P"    `"YbbdP'Y8   `"Ybbd8"'  `"YbbdP"'  `"YbbdP"'  88  88       88   `"YbbdP"Y8       `"Y88888P"   `"8bbdP"Y8  88      88      88   `"Ybbd8"'  
                                                                                aa,    ,88                                                                
                                                                                 "Y8bbdP"                                                                 

    
    """
)
run_game()









