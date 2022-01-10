# CEASER CIPHER GAME 
from typing import DefaultDict
import data

# ask user message 
def ask_user_message():
    user_message = input("Hi! Enter your message: ")
    return user_message

# script direction 

def script_direction():
    direction = input('Enter "encode" to encode and "decode" to decode, "q" to quit the program: ')
    return direction

# encoding message 
def encode_message(message,shift):
    encoded_message_list = []
    for i in range(0,len(message)):
        encoded_message_list.append(data.alphabet[data.alphabet.index(message[i]) + shift])

    return "".join(encoded_message_list)


# decode message
def decode_message(message,shift):
    decoded_message_list = []
    for i in range(0,len(message)):
        decoded_message_list.append(data.alphabet[data.alphabet.index(message[i]) - shift])
    
    return "".join(decoded_message_list)

# run script 

def run_script():
    end_script = False 

    while end_script == False:
        direction = script_direction()
        message = ask_user_message()

        if direction == "encode":
            shift = int(input("Enter shift: "))
            encoded_message = encode_message(message, shift)
            print(f"The incoded message is {encoded_message}")
            continue_flow  = input("Do you want to continue? ")
            if continue_flow == "n":
                print("Program is terminated")
                end_script = True

        elif direction == "decode":
            shift = int(input("Enter shift: "))
            decoded_message = decode_message(message, shift)
            print(f"The Decoded message is {decoded_message}")
            continue_flow  = input("Do you want to continue? ")
            if continue_flow == "n":
                print("Program is terminated")
                end_script = True
        
        elif direction == "q":
            print("Program is terminated")
            end_script = True

        else:
            print("Invalid entry")
            continue




run_script()

 