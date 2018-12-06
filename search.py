import numpy as np 
import board
from heuristic import man_dist 
from item import INITIAL,LIMIT,SAMPLE,SOLUTION,is_equal,get_extra,count_depth,count_pegs
from mynode import MyNode
from time import time
from operator import itemgetter
from pprint import pprint 

TIME_LIMIT = 100 #seconds

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
    print(sol_node.depth_level)
    pprint(sol_node.board)
    parent_node = sol_node.parent
    if (parent_node != None):
        print_parents(parent_node)


def bfs(cur_node,point_table):
    NODE_COUNT = 1
    print("Bread First Search")
    print("Time Limit is 1 Hour")
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
        IS_SUB = not((cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL)))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = time() > TIME_LIMIT +  start        
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("While Count:",WHILE_COUNT)
            print("Sub optimal solution found.”")
            print_parents(SUB_OPTIMAL)
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)    
            break
        if(WHILE_COUNT%10 == 0):
            print("Tur: ",WHILE_COUNT)
        if FRONTIER_LIST[0] =="flag":
            FRONTIER_LIST.pop(0)
        move_list = list_possible_moves(cur_node.board)
        move_list.sort(reverse=True)
        NODE_COUNT += int(len(move_list))
        SUB_FRONT_LIST = []
        for new_states in move_list:
            peg_x,peg_y, way = int(new_states[0]),int(new_states[1]),new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            new_board = board.make_move(np.copy(cur_node.board),peg_x,peg_y,way)
            new_node = MyNode(new_board,cur_node,(count_depth(cur_node)+1),count_pegs(cur_node))
            SUB_FRONT_LIST.append((move_value,new_node))
        SUB_FRONT_LIST.sort(key=itemgetter(0))
        for everything in SUB_FRONT_LIST:
            FRONTIER_LIST.append(everything)
        if FRONTIER_LIST:
            FRONTIER_LIST_LEN = len(FRONTIER_LIST)
            list_element = FRONTIER_LIST.pop(0)
            cur_node = list_element[1]
            IS_FOUND = is_equal(cur_node.board,SOLUTION)
            #IS_FOUND = WHILE_COUNT > 400
            if(IS_FOUND):
                print("------------------------------------------------------------------------")
                print("WHILE_COUNT: ", WHILE_COUNT)
                print("“Optimum solution found.”")
                print_parents(cur_node)
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                return True
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            cur_node = None
            return True
        WHILE_COUNT += 1


def ids_bfs(cur_node,point_table,depth_level_param):
    NODE_COUNT = 1
    print("Bread First Search For Depth: ",depth_level_param)
    print("Time Limit is 1 Hour")
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
        if(cur_node.depth_level > depth_level_param):
            return SUB_OPTIMAL
        IS_SUB = not((cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL)))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = time() > TIME_LIMIT +  start        
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("While Count:",WHILE_COUNT)
            print("Sub optimal solution found.”")
            print_parents(SUB_OPTIMAL)
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)    
            break
        if(WHILE_COUNT%10 == 0):
            print("Tur: ",WHILE_COUNT)
        if FRONTIER_LIST[0] =="flag":
            FRONTIER_LIST.pop(0)
        move_list = list_possible_moves(cur_node.board)
        move_list.sort(reverse=True)
        NODE_COUNT += int(len(move_list))
        SUB_FRONT_LIST = []
        for new_states in move_list:
            peg_x,peg_y, way = int(new_states[0]),int(new_states[1]),new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            new_board = board.make_move(np.copy(cur_node.board),peg_x,peg_y,way)
            new_node = MyNode(new_board,cur_node,(count_depth(cur_node)+1),count_pegs(cur_node))
            SUB_FRONT_LIST.append((move_value,new_node))
        SUB_FRONT_LIST.sort(key=itemgetter(0))
        for everything in SUB_FRONT_LIST:
            FRONTIER_LIST.append(everything)
        if FRONTIER_LIST:
            FRONTIER_LIST_LEN = len(FRONTIER_LIST)
            list_element = FRONTIER_LIST.pop(0)
            cur_node = list_element[1]
            IS_FOUND = is_equal(cur_node.board,SOLUTION)
            #IS_FOUND = WHILE_COUNT > 400
            if(IS_FOUND):
                print("------------------------------------------------------------------------")
                print("WHILE_COUNT: ", WHILE_COUNT)
                print("“Optimum solution found.”")
                print_parents(cur_node)
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                return True
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            cur_node = None
            return True
        WHILE_COUNT += 1



def dfs(cur_node,point_table):
    NODE_COUNT = 1
    print("Depth First Search")
    print("Time Limit is 1 Hour")
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
        IS_SUB = not((cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL)))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = time() > TIME_LIMIT +  start        
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("While Count:",WHILE_COUNT)
            print("Sub optimal solution found.”")
            print_parents(SUB_OPTIMAL)
            print("Total Run Time: ",time()-start)
            print("Total Nodes Expanded: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)    
            break
        if(WHILE_COUNT%10 == 0):
            print("Tur: ",WHILE_COUNT)
        if FRONTIER_LIST[0] =="flag":
            FRONTIER_LIST.pop(0)
        move_list = list_possible_moves(cur_node.board)
        move_list.sort(reverse=True)
        NODE_COUNT += int(len(move_list))
        SUB_FRONT_LIST = []
        for new_states in move_list:
            peg_x,peg_y, way = int(new_states[0]),int(new_states[1]),new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            new_board = board.make_move(np.copy(cur_node.board),peg_x,peg_y,way)
            new_node = MyNode(new_board,cur_node,(count_depth(cur_node)+1),count_pegs(cur_node))
            SUB_FRONT_LIST.append((move_value,new_node))
        for everything in SUB_FRONT_LIST:
            FRONTIER_LIST.append(everything)
        if FRONTIER_LIST:
            FRONTIER_LIST_LEN = len(FRONTIER_LIST)
            list_element = FRONTIER_LIST.pop(FRONTIER_LIST_LEN-1)
            cur_node = list_element[1]
            IS_FOUND = is_equal(cur_node.board,SOLUTION)
            #IS_FOUND = WHILE_COUNT > 400
            if(IS_FOUND):
                print("------------------------------------------------------------------------")
                print("WHILE_COUNT: ", WHILE_COUNT)
                print("“Optimum solution found.”")
                print_parents(cur_node)
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                return True
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            cur_node = None
            return True
        WHILE_COUNT += 1

def ids(cur_node,point_table):
    SUB_OPTIMAL_SOL = cur_node
    for iteration in range(32):
        SUB_OPTIMAL_SOL = ids_bfs(cur_node,point_table,iteration)
    return True

def dfs_rand(cur_node):
    pass

def dfs_spec(cur_node):
    NODE_COUNT = 1
    print("Depth First Search with Special Selection")
    print("Time Limit is 1 Hour")
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
        IS_SUB = not((cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL)))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = time() > TIME_LIMIT +  start
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("While Count:",WHILE_COUNT)
            print("Sub optimal solution found.”")
            print_parents(SUB_OPTIMAL)
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)            
            break
        #if(WHILE_COUNT%10 == 0):
        #    print("Tur: ",WHILE_COUNT)
        if FRONTIER_LIST[0] =="flag":
            FRONTIER_LIST.pop(0)
        move_list = list_possible_moves(cur_node.board)
        NODE_COUNT += int(len(move_list))
        SUB_FRONT_LIST = []
        for new_states in move_list:
            peg_x, peg_y, way = int(new_states[0]),int(new_states[1]),new_states[2]
            new_board = board.make_move(np.copy(cur_node.board),peg_x,peg_y,way)
            move_value = man_dist(new_board)
            new_node = MyNode(new_board,cur_node,(count_depth(cur_node)+1),count_pegs(cur_node))
            SUB_FRONT_LIST.append((move_value,new_node))
        SUB_FRONT_LIST.sort(key=itemgetter(0))
        for everything in SUB_FRONT_LIST:
            FRONTIER_LIST.append(everything)
        if FRONTIER_LIST:
            FRONTIER_LIST_LEN = len(FRONTIER_LIST)
            list_element = FRONTIER_LIST.pop(FRONTIER_LIST_LEN-1)
            cur_node = list_element[1]
            IS_FOUND = is_equal(cur_node.board,SOLUTION) 
            #IS_FOUND = WHILE_COUNT > 20
            if(IS_FOUND):
                print("----------------------------------------------")
                print("WHILE_COUNT: ", WHILE_COUNT)
                print("“Optimum solution found.”")
                print_parents(cur_node)
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                return True
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            cur_node = None
            return True
        WHILE_COUNT +=1