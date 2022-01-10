# CALCULATOR PROGRAM 
import asci_art

# ask for operations 

def get_result():
    operators = ["/","+","-","*"]
    num_1 = int(input("Enter first number: "))
    operator = input("Enter the operation to perform: ")
    num_2 = int(input("Enter second number: "))

    if operators.index(operator) == -1:
        print("Invalid operator")
    else: 
        if operator == operators[0]:
            print(divide_num(num_1, num_2))
            
            
# add numbers
def add_num(num1,num2):
    return num1 + num2

# subtract numbers 
def subtract_num(num1,num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1 

# divide numbers 
def divide_num(num1,num2):
    if num1 > num2:
        return num1 / num2
    else:
        return num2 / num1 


# multiply numbers 
def multiply_num(num1,num2):
    return num1 * num2 


get_result()

