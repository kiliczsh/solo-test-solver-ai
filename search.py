import numpy as np 
import board
import heuristic as heu
from item import INITIAL,LIMIT,SAMPLE,SOLUTION,is_equal,get_extra
from mynode import MyNode
from time import sleep,time


def list_possible_moves(board_array_param):
    fun_move_list = []
    for i in range(LIMIT):
        for j in range(LIMIT):
            #print(type(board_array_param))
            #print(board_array_param)
            current_square = int(board_array_param[i,j])
            bannned_square = (i==0 or i==1 or i==5 or i==6) and (j==0 or j==1 or j==5 or j==6)
            if(not bannned_square):
                if(current_square == 1):
                    try:
                        right_square = None
                        if(j+2 < LIMIT ):
                            right_square = int(board_array_param[i,j+2])
                            gap_peg = int(board_array_param[i,j+1])
                        if(right_square == 0 and gap_peg == 1):
                            fun_move_list.append((i,j,"e"))
                    except NameError:
                        right_square = None
                    
                    
                    try:
                        left_square = None
                        if( j-2 >= 0):
                            left_square = int(board_array_param[i,j-2])
                            gap_peg = int(board_array_param[i,j-1])
                        if(left_square == 0 and gap_peg == 1):
                            fun_move_list.append((i,j,"w"))
                    except NameError:
                        left_square = None
                    
                    
                    try:
                        down_square = None
                        if(i+2 < LIMIT):
                            down_square = int(board_array_param[i+2,j])
                            gap_peg = int(board_array_param[i+1,j])
                        if(down_square == 0 and gap_peg == 1):
                            fun_move_list.append((i,j,"s"))
                    except NameError:
                        down_square = None
            

                    try:
                        up_square = None
                        if(i-2 >= 0):
                            up_square = int(board_array_param[i-2,j])
                            gap_peg = int(board_array_param[i-1,j])
                        if(up_square == 0 and gap_peg == 1 ):
                            fun_move_list.append((i,j,"n"))
                    except NameError:
                        up_square = None
    
    return fun_move_list

def print_parents(sol_node):
    print(sol_node.board)
    print(sol_node.parent)
    parent_node = sol_node.parent
    if (parent_node != None):
        print_parents(parent_node)


def dfs(cur_node,point_table):
    
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    TIME_LIMIT = 3600 #seconds
    start = time()
    while FRONTIER_LIST:
        IS_TIME_OUT = time() > TIME_LIMIT +  start
        if(IS_TIME_OUT):
            break
        if FRONTIER_LIST[0] =="flag":
            FRONTIER_LIST.pop(0)
        if(WHILE_COUNT%1000 == 0):
            print("Tur: ",WHILE_COUNT)
        move_list = list_possible_moves(cur_node.board)
        move_list.sort(reverse=True)
        for new_states in move_list:
            peg_x,peg_y, way = int(new_states[0]),int(new_states[1]),new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            new_board = board.make_move(np.copy(cur_node.board),peg_x,peg_y,way)
            new_node = MyNode(new_board,cur_node)
            FRONTIER_LIST.append((move_value,new_node))
            IS_FOUND = is_equal(new_node.board,SOLUTION)    
            #IS_FOUND = WHILE_COUNT > 30000
            if(IS_FOUND):
                print("WHILE_COUNT: ", WHILE_COUNT)
                print("AWESOME")
                print_parents(new_node)
                return True                       
        if FRONTIER_LIST:
            FRONTIER_LIST_LEN = len(FRONTIER_LIST)
            cur_fr_list_element = FRONTIER_LIST.pop(FRONTIER_LIST_LEN-1)
            cur_node = cur_fr_list_element[1]
        else:
            print("DONE")
            cur_node = None
            return True
        WHILE_COUNT +=1
    print("Count: ",WHILE_COUNT)
    #7667769. sırada sonuç buldu #TODO

def dfs_spec(cur_node,point_table):
    
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    TIME_LIMIT = 3600 #seconds
    start = time()
    while FRONTIER_LIST:
        IS_TIME_OUT = time() > TIME_LIMIT +  start
        if(IS_TIME_OUT):
            break
        if FRONTIER_LIST[0] =="flag":
            FRONTIER_LIST.pop(0)
        if(WHILE_COUNT%1000 == 0):
            print("Tur: ",WHILE_COUNT)
        move_list = list_possible_moves(cur_node.board)
        move_list.sort(reverse=True)
        for new_states in move_list:
            peg_x,peg_y, way = int(new_states[0]),int(new_states[1]),new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            new_board = board.make_move(np.copy(cur_node.board),peg_x,peg_y,way)
            move_value = heu.man_dist(new_board)
            new_node = MyNode(new_board,cur_node)
            FRONTIER_LIST.append((move_value,new_node))
            IS_FOUND = is_equal(new_node.board,SOLUTION)    
            #IS_FOUND = WHILE_COUNT > 30000
            if(IS_FOUND):
                print("WHILE_COUNT: ", WHILE_COUNT)
                print("AWESOME")
                print_parents(new_node)
                return True                       
        if FRONTIER_LIST:
            FRONTIER_LIST_LEN = len(FRONTIER_LIST)
            cur_fr_list_element = FRONTIER_LIST.pop(FRONTIER_LIST_LEN-1)
            cur_node = cur_fr_list_element[1]
        else:
            print("DONE")
            cur_node = None
            return True
        WHILE_COUNT +=1
    print("Count: ",WHILE_COUNT)