# SILENT BIDDING ACUCTION 



#  get user name and bid 

def ask_user_details():
    user_name = input('Enter your Name: ')
    user_bid = int(input("Entrer your Bid: $"))
    return {
        "name":user_name,
        "bid":user_bid,
    }

# check for highest bidder
def check_highest_bidder(list):
    bids_list = []
    for item in list:
        bids_list.append(item["bid"])

    heighest_bidder_obj = list[bids_list.index(max(bids_list))]
    print(f"{heighest_bidder_obj['name']} has the heighest bid of {heighest_bidder_obj['bid']}")


# run program 
def run_program():
    bidders_list = []
    stop_program = False 

    while stop_program == False:
        user_obj = ask_user_details()
        bidders_list.append(user_obj)
        print(bidders_list)
        continue_flag = input("Are there other users? 'y' for yes 'n' for no: ")
        if continue_flag == "n":
            check_highest_bidder(bidders_list)
            stop_program = True
            print("The program is terminated")

        elif continue_flag == "y":
            continue
        else: 
            print('Invalid Entry, Try Again')
            continue

run_program()



