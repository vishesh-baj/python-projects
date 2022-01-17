import random
import art
from game_data import data


# comparing list
def comparing_list():
    compare_list = [random.choice(data), random.choice(data)]
    return compare_list

# opeaning text

def opening_text(name_1,name_2):
    print(art.logo)
    print(f"{name_1}   {art.vs}  {name_2}")


# check who has more follows 
def check_followers(compare_list):
    followers_count_1 = compare_list[0]["follower_count"]
    followers_count_2 = compare_list[1]["follower_count"]
    random_name_1 = compare_list[0]["name"]
    random_name_2 = compare_list[1]["name"]
    user_comparision = int(input(f"Enter '1' to select {compare_list[0]['name']}, Enter '2' to select {compare_list[1]['name']} "))
    max_followers = max(followers_count_1,followers_count_2)

    if max_followers == followers_count_1 and user_comparision == 1:
        return True 
    elif max_followers == followers_count_2 and user_comparision == 2:
        return True
    else:
        return False

# run game 

def run_game():

    game_over = False 
    score = 0 
   
    while not game_over:
        comparision_lst =  [random.choice(data), random.choice(data)]
        opening_text(comparision_lst[0]["name"], comparision_lst[1]["name"])
        choice = check_followers(comparision_lst)
        if choice == False:
            print(f"You  guessed wrong, Your total score is: {score}")
            print("GAME OVER")
            game_over = True
        else: 
            score += 1
            print("You guessed correctlty")
            print(f"Your score is {score}")

run_game()










    
