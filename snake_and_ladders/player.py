# PLAYER CLASS
import random
class Player:
    def __init__(self,name):
        self.name = name
        self.position = 0

    def throw_dice(self):
        random_dice_value = random.randint(1, 6)
        self.position += random_dice_value
        


