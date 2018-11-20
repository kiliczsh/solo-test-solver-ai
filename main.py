import board
import path
import heuristic
import search
import numpy as np
from anytree import Node, RenderTree


# ---------------------------------------- functions ---------------------------------------

def create_and_add(acker,prev_board,move_list):
    for x in range(len(move_list)):
        next_board = game_board.make_move(np.copy(prev_board),move_list[x][0],move_list[x][1],move_list[x][2] )
        #print("\nBoard Man: ",heuristic.man_dist(next_board),"\n\n")
        Node(next_board,parent=acker)
    return acker

def print_tree_of(parent_node):
    for pre, fill, node in RenderTree(parent_node):
        print("%s*\n%s" % (pre, node.name))


# ------------------------------------------  main -----------------------------------------


if __name__ == "__main__":

    game_board = board.Board(['n', 'e', 's', 'w'],
                  np.array([[2, 2, 1, 1, 1, 2, 2],
                            [2, 2, 1, 1, 1, 2, 2],
                            [1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 0, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1],
                            [2, 2, 1, 1, 1, 2, 2],
                            [2, 2, 1, 1, 1, 2, 2]],dtype=np.int))
    point_table = game_board.create_square_points()

    initial_board = np.copy(game_board.board_array)

    search.bfs(initial_board,point_table)


    #man_dist_val = heuristic.man_dist(initial_board)
    #move_list = game_board.list_possible_moves(initial_board)
    #root = Node(initial_board)
    #root = create_and_add(root,initial_board,move_list) #TODO

    #for element in RenderTree(root):
    #    current_board = element.node.name
    #    current_move_list = game_board.list_possible_moves(current_board)
    #    print(current_board)

    #print_tree_of(root)

    """
    game_board.play_game()
    game_board.print_board()

    if(game_board.check_win()):
        print("You are too good")
    else:
        print("You get an unoptimized solution")
    """



