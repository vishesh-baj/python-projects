# BOARD CLASS 

class Board:
    def __init__(self, board_size):
        self.board_size = board_size

    def create_board(self):
        board = [x for x in range(0,self.board_size)]
        return board

