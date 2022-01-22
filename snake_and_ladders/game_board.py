# GAME BOARD CLASS

class Board: 
    def __init__(self,board_size, ladder_positions, snake_positions):
        self.board_size = board_size 
        self.ladder_positions = ladder_positions
        self.snake_positions = snake_positions
        # initializing generatwe_board function at the instansiation of the object 
        self.generate_board()

    def generate_board(self):
        game_board = [x for x in range(0,self.board_size)]
        return game_board

    
    


    

