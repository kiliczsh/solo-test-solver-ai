import board
import path
import heuristic
from search import dfs,dfs_spec
import numpy as np
from mynode import MyNode
from item import INITIAL
from time import sleep,time

# ------------------------------------------  main -----------------------------------------


if __name__ == "__main__":
    start = time()
    #SETUP
    game_board = board.Board(['n', 'e', 's', 'w'],INITIAL)
    point_table = game_board.create_square_points()
    initial_board = np.copy(game_board.board_array)
    initial_node = MyNode(initial_board,None)
    result = dfs_spec(initial_node,point_table)

