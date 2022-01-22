# PLAYER CLASS 
import random

class Player:
    def __init__(self,player_count):
        self.player_count = player_count
        self.registered_players = []

    def register_players(self):
        for i in range(self.player_count):
            player_name = input(f"Enter Player {i + 1} name: ")
            self.registered_players.append({"name": player_name, "position": 0})

    def player_turn(self):
        for player in self.registered_players:
            dice_roll_trigger = int(input(f"{player} its your turn, press 1 to roll a dice: "))
            if dice_roll_trigger == 1:
                dice_value = random.randint(1, 6)
                print(f'{player}, your dice value is {dice_value}')
                self.registered_players[0]['position'] += dice_value
            else:
                print("Enter cottect value")





    
