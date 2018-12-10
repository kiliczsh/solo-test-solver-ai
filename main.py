import board
import heuristic
import numpy as np
from search import bfs,dfs,ids,dfs_rand,dfs_spec,ids_bfs
from mynode import MyNode
from item import INITIAL,DIRECTION,POINT_TABLE
from time import sleep,time
from sys import argv

# ------------------------------------------  main -----------------------------------------


if __name__ == "__main__":
    #SETUP
    game_board = board.Board(DIRECTION,INITIAL)
    initial_board = np.copy(game_board.board_array)
    initial_node = MyNode(initial_board,None,0,32)
    # arguments assigment
    method = int(argv[1])
    TIME_LIMIT = int(argv[2])

    if(method == 1): 
        result_1 = bfs(initial_node,POINT_TABLE,TIME_LIMIT)
    elif(method == 2): 
        result_2 = dfs(initial_node,POINT_TABLE,TIME_LIMIT)
    elif(method == 3): 
        result_3 = ids(initial_node,POINT_TABLE,TIME_LIMIT)
    elif(method == 4): 
        result_4 = dfs_rand(initial_node,POINT_TABLE,TIME_LIMIT)
    elif(method == 5):
        result_5 = dfs_spec(initial_node,TIME_LIMIT)
    else:
        print("\n1-) Breadth First Search\n2-) Depth First Search\n3-) Iterative Deepening Search\n4-) Depth First with Random")
        print("5-) Depth First with Heuristic")
