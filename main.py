import board
import path
import heuristic
from search import bfs,dfs,ids,dfs_rand,dfs_spec
import numpy as np
from mynode import MyNode
from item import INITIAL,DIRECTION,POINT_TABLE,MY_POINT_TABLE,MY_POINT_TABLE_TWO
from time import sleep,time

# ------------------------------------------  main -----------------------------------------


if __name__ == "__main__":
    start = time()
    #SETUP
    game_board = board.Board(DIRECTION,INITIAL)
    initial_board = np.copy(game_board.board_array)
    initial_node = MyNode(initial_board,None,0,32)
    #result_1 = bfs(initial_node,POINT_TABLE)
    #result_2 = dfs(initial_node,MY_POINT_TABLE_TWO)
    #result_3 = ids(initial_board,POINT_TABLE)
    #result_4 = dfs_rand(initial_board)
    result_5 = dfs_spec(initial_node)

