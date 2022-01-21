# Board class
import random

class Board:

    def __init__(self,board_size):
        # initial attributes for the object 
        self.board_size = board_size
        self.ladder_count = ladder_count
        # self.snake_count = snake_count
        self.ladder_positions = ladder_positions
        self.snake_positions = snake_positions

    def create_board(self):
        board_list = [x for x in range(1, self.board_size + 1)]
        print(board_list)
       


