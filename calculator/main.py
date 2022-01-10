# CALCULATOR PROGRAM 
import asci_art

# ask for operations 

            
            
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

# check operationds 
def find_answer(inp_1, inp_2, operator):
    if operator == "*":
        return multiply_num(inp_1, inp_2)
    elif operator == "+":
        return  add_num(inp_1, inp_2)
    elif operator == "-":
        return subtract_num(inp_1,inp_2)
    elif operator == "/":
        return divide_num(inp_1,inp_2)

# run program 


def run_program():
    
    end_program = False 

    input_1 = int(input("Enter first number: "))
    input_2 = int(input("Enter second number:" ))
    operation = input("Enter the operation to perform: ")

    answer = find_answer(input_1,input_2,operation)


    while not end_program:
        choice = input(f"Your answer is: {answer},\nPress n to operate with new number, press 'q' to quit: ")

        if choice == "q":
            print("Program Stopped!")
            end_program = True
        elif choice == "n":
            operation_2 = input("Enter the operation: ")
            input_3 = int(input("Enter number: "))
            answer = find_answer(answer,input_3,operation_2)

        else: 
            print("Invalid Response!")
    

            


run_program()
