# SNAKE AND LADDERS GAME
from game_board import  Board
from player import Player


player = Player(2)
game_board = Board(100, 2, 2)
player.register_players()
player.player_turn()

