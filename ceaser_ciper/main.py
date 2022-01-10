# CEASER CIPHER GAME 
import data
# ask user name 
def ask_user_name():
    user_name = input("Enter Username: ")
    return user_name

# ask user message 
def ask_user_message(username):
    user_message = input(f"Hi {username}! Enter your message: ")
    return user_message

# script direction 

def script_direction():
    direction = input('Enter "encode" to encode and "decode" to decode, "q" to quit the program: ')
    return direction

# encoding message 
def encode_message(message):
    shift = int(input("Enter the shift: "))
    encoded_list = []
    encoded_message = []

    for i in range(0,len(message)):
        for j in range(0,len(data.alphabet)):
            if data.alphabet[j] == message[i]:
                encoded_list.append(j + shift)
    
    for i in range(0,len(encoded_list)):
        encoded_message.append(data.alphabet[encoded_list[i]])
    
    return "".join(encoded_message)


# decoding message 
def decode_message(message):
    shift = int(input("Enter the shift: "))

    decoded_list = []
    decoded_message = []

    for i in range(0,len(message)):
        for j in range(0,len(data.alphabet)):
            if data.alphabet[j] == message[i]:
                decoded_list.append(j - shift)

    for i in range(0,len(decoded_list)):
        decoded_message.append(data.alphabet[decoded_list[i]])

    return "".join(decoded_message)






# run the script 
def run_script():
    end_script = False 

    while end_script == False:
        user_name = ask_user_name()
        direction = script_direction()
        continue_script = input('Do you want to continue the script? "Y" for yes and "N" for no ')

        if continue_script == "y":
            if direction == "encode":
                message = ask_user_message(user_name)
                encoded_message = encode_message(message)
                print(f"Your encoded message is: {encoded_message}")

        
            elif direction == "decode":
                message = ask_user_message(user_name)
                decoded_message = decode_message(message)
                print(f"Your decoded message is {decoded_message}")
            
            elif direction == "q":
                print('You have choosen to quit the script')
                print("Program Terminated")
                end_script =True
                


            else: 
                print("Script ended")
                end_script = True
        elif continue_script == "n":
            print("Script is terminated")
            end_script = True

        else: 
            print("Invalid Entry, Script Ended")
            
        
        





print(run_script())


