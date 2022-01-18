from menu import MENU
from resources import resources

is_on = True
profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made , False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'"Sorry there is not enough {item}"')
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment ius accepted or False if payment is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money")
        return False


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .01
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


while is_on:
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        for key in resources:
            print(f'{key}: {resources[key]}')
        print(profit)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            is_transaction_successful(payment, drink['cost'])











