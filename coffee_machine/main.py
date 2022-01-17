from resources import resources
from menu import MENU


# prompt user 

def ask_user_input():
    user_choice = input("What do you want? espresso/Latte/Cappuccino: ")
    return user_choice

# check availablity 

def check_availablity(beverage):
    if beverage == 'espresso':
        water_availablity = resources['water'] >= MENU[beverage]['ingredients']['water']
        coffee_availablity = resources['coffee'] >= MENU[beverage]['ingredients']['coffee']
        if water_availablity and coffee_availablity:
            print(f"Your total is {MENU[beverage]['cost']}")
        else:
            print("Beverage cannot be made")

    elif beverage == "latte":
        water_availablity = resources['water'] >= MENU[beverage]['ingredients']['water']
        coffee_availablity = resources['coffee'] >= MENU[beverage]['ingredients']['coffee']
        milk_availablity = resources['milk'] >= MENU[beverage]['ingredients']['milk']
    
    elif beverage == 'cappuccino':
        water_availablity = resources['water'] >= MENU[beverage]['ingredients']['water']
        coffee_availablity = resources['coffee'] >= MENU[beverage]['ingredients']['coffee']
        milk_availablity = resources['milk'] >= MENU[beverage]['ingredients']['milk']






# function to run script 
def run_script():

    machine_off = False 

    while not machine_off:
        user_choice = ask_user_input()
        if user_choice == "off":
            print("System Shutting Down")
            machine_off = True

        elif  user_choice == "report":
            print("RESOURCE REPORTS")
            for key in resources:
                print(f"{key}: {resources[key]}")
        elif user_choice == "espresso":
            check_availablity(user_choice)
            
            


run_script()






