import numpy as np 
import psutil
import board
import zmq
from item import INITIAL,LIMIT,SOLUTION,is_equal,get_extra,count_depth,count_pegs
from item import list_possible_moves,print_parents
from operator import itemgetter
from heuristic import man_dist 
from random import shuffle
from pprint import pprint
from mynode import MyNode
from time import time,sleep


def bfs(cur_node,point_table,time_limit):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5558")
    try:  
        NODE_COUNT = 1
        print("Breadth First Search")
        print("Time Limit is ",time_limit," seconds.")
        TIME_LIMIT = time_limit
        FRONTIER_LIST = [("flag",cur_node)]
        WHILE_COUNT = 0
        start = time()
        SUB_OPTIMAL = cur_node
        while FRONTIER_LIST:
            if(WHILE_COUNT%100 ==0 ):
                print("Tur: ", WHILE_COUNT)
            IS_SUB = not((cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL)))
            if(IS_SUB):
                SUB_OPTIMAL = cur_node
            IS_TIME_OUT = int(time()) > int(TIME_LIMIT) +  int(start)
            if(psutil.virtual_memory().free < 125000000): 
                print("MEMORY OUT")
                print("Sub optimal solution found.")
                print("Total Run Time: ",time() - start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)    
                print_parents(SUB_OPTIMAL)
                break
            if(IS_TIME_OUT):
                print("TIME IS OUT")
                print("Sub optimal solution found.")
                print("Total Run Time: ",time() - start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)    
                print_parents(SUB_OPTIMAL)
                break
            if FRONTIER_LIST[0][0] =="flag":
                FRONTIER_LIST.pop(0)
            move_list = list_possible_moves(cur_node.board)
            move_list.sort(reverse=True)
            NODE_COUNT += int(len(move_list))
            # create new boards from move_list and add to SUB_FRONT_LIST
            SUB_FRONT_LIST = []
            for new_states in move_list:
                peg_x,peg_y, way = int(new_states[0]),int(new_states[1]),new_states[2]
                free_x,free_y = get_extra(peg_x,peg_y,way)
                move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
                new_board = board.make_move(np.copy(cur_node.board),peg_x,peg_y,way)
                new_node = MyNode(new_board,cur_node,(count_depth(cur_node)+1),count_pegs(cur_node))
                SUB_FRONT_LIST.append((move_value,new_node))
            SUB_FRONT_LIST.sort(key=itemgetter(0))
            # add all new boards in an order to FRONTIER_LIST
            for everything in SUB_FRONT_LIST:
                FRONTIER_LIST.append(everything)
            if FRONTIER_LIST:
                # choose new board node to continue searching and check if is it a solution
                FRONTIER_LIST_LEN = len(FRONTIER_LIST)
                list_element = FRONTIER_LIST.pop(0)
                cur_node = list_element[1]
                IS_FOUND = is_equal(cur_node.board,SOLUTION)
                if(IS_FOUND):
                    print("Optimum solution found.")
                    print("VM Used: ",psutil.virtual_memory().used)
                    print("VM Free: ",psutil.virtual_memory().free)
                    print("Total Run Time: ",time()-start)
                    print("Frontier Length: ",len(FRONTIER_LIST))
                    print("Node Visited: ",NODE_COUNT)
                    print_parents(cur_node)
                    return True
            else:
                print("NOTHING LEFT BEHIND")
                print("Total Run Time: ",time()-start)
                cur_node = None
                return True
            WHILE_COUNT += 1
    except KeyboardInterrupt:
        print("Sub optimal solution found.")
        print("VM Used: ",psutil.virtual_memory().used)
        print("VM Free: ",psutil.virtual_memory().free)
        print("Total Run Time: ",time() - start)
        print("Frontier Length: ",len(FRONTIER_LIST))
        print("Node Visited: ",NODE_COUNT)    
        print_parents(SUB_OPTIMAL)
    finally:
        socket.close()
        context.term()    
    return SUB_OPTIMAL

def dfs(cur_node,point_table,time_limit):
    NODE_COUNT = 1
    print("Depth First Search")
    print("Time Limit is ",time_limit," seconds.")
    TIME_LIMIT = time_limit
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
    
        if(count_pegs(cur_node) <= 1):
            print_parents(cur_node)
            print("done")
            return
        IS_SUB = (cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = int(time()) > int(TIME_LIMIT) +  int(start)        
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("While Count:",WHILE_COUNT)
            print("Sub optimal solution found.")
            print("Total Run Time: ",time()-start)
            print("Total Nodes Expanded: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)
            print_parents(SUB_OPTIMAL)
            break
        if FRONTIER_LIST[0][0] =="flag":
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
            list_element = FRONTIER_LIST.pop(FRONTIER_LIST_LEN-1)
            cur_node = list_element[1]
            IS_FOUND = is_equal(cur_node.board,SOLUTION)
            if(IS_FOUND):
                print("Optimum solution found.")
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                print_parents(cur_node)
                return True
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)
            cur_node = None
            return True
        WHILE_COUNT += 1

def ids(cur_node,point_table,time_limit):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5558")
    try:  
        start = time()
        print("Iterative Deepening Search")
        print("Time Limit is ",time_limit," seconds.")
        SUB_OPTIMAL_SOL = cur_node
        # for each depth level make depth limited bread
        for iteration in range(33):
            IS_TIME_OUT = time() > time_limit +  start
            new_time_limit = time_limit - (time()-start)
            print("----------------------------------------------")
            if(IS_TIME_OUT):
                print("TIME IS OUT FOR IDS")
                print("Sub optimal solution found.”")
                print("Total Run Time: ",time()-start)
                print_parents(SUB_OPTIMAL_SOL)
                break
            SUB_OPTIMAL_SOL = ids_bfs(cur_node,point_table,iteration,new_time_limit)
    except KeyboardInterrupt:
        print_parents(SUB_OPTIMAL_SOL)
    finally:
        socket.close()
        context.term()    
    return SUB_OPTIMAL_SOL

def ids_bfs(cur_node,point_table,depth_level_param,time_limit): 
    NODE_COUNT = 1
    print("IDS For Depth: ",depth_level_param)
    print("Time Limit is ",time_limit," seconds.")
    TIME_LIMIT = time_limit
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
        IS_DEPTH_GOAL = cur_node.depth_level > depth_level_param
        if(IS_DEPTH_GOAL):
            print("Depth limit is over.")
            print("Depth ",cur_node.depth_level - 1 ," completed.")
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)
            print()
            return SUB_OPTIMAL
        IS_SUB = (cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = int(time()) > int(TIME_LIMIT) +  int(start)      
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("Sub optimal solution found.")
            print("Sub optimal solution located at depth: ",SUB_OPTIMAL.depth_level)
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)
            #print_parents(SUB_OPTIMAL)
            print()
            return SUB_OPTIMAL
        if (FRONTIER_LIST[0][0] == "flag"):
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
            IS_FOUND = is_equal(cur_node.board,SOLUTION) and (cur_node.depth_level >= 31)
            if(IS_FOUND):
                print("Optimum solution found for depth: ",cur_node.depth_level - 1)
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                print_parents(cur_node)
                print()
                return cur_node
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)
            cur_node = None
            return SUB_OPTIMAL
        WHILE_COUNT += 1

def dfs_rand(cur_node,point_table,time_limit):
    NODE_COUNT = 1
    print("Depth First Search with Random Selection")
    print("Time Limit is ",time_limit," seconds.")
    TIME_LIMIT = time_limit
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
        IS_SUB = (cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = int(time()) > int(TIME_LIMIT +  start)   
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("Sub optimal solution found.")
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)
            print_parents(SUB_OPTIMAL)
            break
        if FRONTIER_LIST[0][0] =="flag":
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
        shuffle(SUB_FRONT_LIST)
        for everything in SUB_FRONT_LIST:
            FRONTIER_LIST.append(everything)
        if FRONTIER_LIST:
            FRONTIER_LIST_LEN = len(FRONTIER_LIST)
            list_element = FRONTIER_LIST.pop(FRONTIER_LIST_LEN-1)
            cur_node = list_element[1]
            IS_FOUND = is_equal(cur_node.board,SOLUTION)
            if(IS_FOUND):
                print("“Optimum solution found.”")
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                print_parents(cur_node)
                return True
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)
            cur_node = None
            return True
        WHILE_COUNT += 1
    pass

def dfs_spec(cur_node,time_limit):
    NODE_COUNT = 1
    print("Depth First Search with Special Selection")
    print("Time Limit is 1 Hour")
    TIME_LIMIT = time_limit
    FRONTIER_LIST = [("flag",cur_node)]
    WHILE_COUNT = 0
    start = time()
    SUB_OPTIMAL = cur_node
    while FRONTIER_LIST:
        IS_SUB = (cur_node.depth_level > SUB_OPTIMAL.depth_level) and (count_pegs(cur_node) < count_pegs(SUB_OPTIMAL))
        if(IS_SUB):
            SUB_OPTIMAL = cur_node
        IS_TIME_OUT = int(time()) > int(TIME_LIMIT) +  int(start)
        if(IS_TIME_OUT):
            print("TIME IS OUT")
            print("Sub optimal solution found.")
            print("Total Run Time: ",time()-start)
            print("Frontier Length: ",len(FRONTIER_LIST))
            print("Node Visited: ",NODE_COUNT)            
            print_parents(SUB_OPTIMAL)
            break
        if FRONTIER_LIST[0][0] =="flag":
            FRONTIER_LIST.pop(0)
        move_list = list_possible_moves(cur_node.board)
        move_list.sort(reverse=True)
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
            #IS_FOUND = WHILE_COUNT > 2
            if(IS_FOUND):
                print("Optimum solution found.")
                print("Total Run Time: ",time()-start)
                print("Frontier Length: ",len(FRONTIER_LIST))
                print("Node Visited: ",NODE_COUNT)
                print_parents(cur_node)
                return True
        else:
            print("NOTHING LEFT BEHIND")
            print("Total Run Time: ",time()-start)
            cur_node = None
            return True
        WHILE_COUNT +=1