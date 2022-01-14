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

# generate blank list
def generate_blank_list(word):
    blank_list = []
    for _ in range(0,len(word)):
        blank_list.append("_")
    return blank_list
    



# ask user guess 
def ask_user_guess():
    user_guess = input("Enter your guess: ")
    return user_guess


# run the game 
def run_game():

    user_life = 7
    user_score = 0
    game_over = False
    generated_word = generate_random_word()
    generated_blank_list = generate_blank_list(generated_word)



    while game_over == False:
        print(generated_word)
        user_guess = ask_user_guess()
        letter_check = generated_word.find(user_guess)
        if letter_check == -1:
            if user_life == 1:
                game_over = True
                print("This is your last life you died! Game Over")
            else:
                user_life -= 1 
                print("You have entered a wrong guess and lost one life.")
                print(hangman_pics.HANGMANPICS[user_score])
                print(f"Remaining Life: {user_life}")
        elif letter_check != -1:
            user_score += 1 

            if user_score == len(generated_word):
                print(f"You won! The word was: {generated_word}")
                game_over = True
            
            else:
                generated_blank_list[letter_check] = user_guess
                print("Guessed Correctly")
                print(generated_blank_list)




        else:
            print("Invalid Entry")

        

run_game()



        





