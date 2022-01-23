# SNAKE AND LADDERS GAME 
import board
from player import Player
import random
game_over = False 

board_size = int(input("Enter board size: "))
board_obj = board.Board(board_size)
number_of_players = int(input("Enter number of players playing the game: "))

def return_players_obj(number_of_players):
    players_obj_lst = []
    for i in range(0,number_of_players):
        player_name = input(f"Enter player {i + 1} name: ")
        player = Player(player_name)
        players_obj_lst.append(player)
    
    return players_obj_lst
       

        

while not game_over:
    game_board = board_obj.create_board()
    player_obj_lst = return_players_obj(number_of_players)
    player_obj_lst[0].throw_dice()
    print([player_obj_lst[0].position])
    






    