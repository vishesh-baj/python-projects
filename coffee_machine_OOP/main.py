from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items_obj = Menu()
coffee_machine_items = items_obj.get_items()

coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

machine_on = True 
while machine_on:
    ask_user_input = input(f"Enter the drink {coffee_machine_items}: ")
    item_details = items_obj.find_drink(ask_user_input)
    print(item_details.ingredients)
    if ask_user_input == "report":
        coffee_maker_obj.report()
    if coffee_maker_obj.is_resource_sufficient(item_details):
        if money_machine_obj.make_payment(item_details.cost):
            coffee_maker_obj.make_coffee(item_details)
        else:
            print("payment Failed")
            
    else:
        print("Insufficienrt Resources")


