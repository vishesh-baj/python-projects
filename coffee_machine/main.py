from tkinter import Menu
from menu import MENU
from resources import resources


# ask user for input
def ask_beverage():
        choices = ["espresso","latte","capuccino"]
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice in choices:
            return MENU[user_choice]
        elif user_choice == "q":
            return 0
        elif user_choice == "report":
            return resources
        
   
# check for requirements 

def check_requirements(supply,demand):
    if supply > demand:
        return True
    else: 
        return False


# run script 

def run_script():

    turn_off = False 

    while not turn_off:
       selected_beverage =  ask_beverage()
       


