import numpy as np 
import board
import heuristic as heu
from anytree import Node, RenderTree

LIMIT = 7

SOLUTION = np.array([[2, 2, 0, 0, 0, 2, 2],
                     [2, 2, 0, 0, 0, 2, 2],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [2, 2, 0, 0, 0, 2, 2],
                     [2, 2, 0, 0, 0, 2, 2]])


SAMPLE = np.array([[2, 2, 1, 1, 1, 2, 2],
                   [2, 2, 1, 0, 1, 2, 2],
                   [1, 1, 1, 0, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1],
                   [2, 2, 1, 1, 1, 2, 2],
                   [2, 2, 1, 1, 1, 2, 2]])


def get_extra(x,y,direction):
    if( (direction == "s") ):
        if(x+2 < 7 ):
            return x+2,y
    if( (direction == "e") ):
        if(y+2 < 7):   
            return x,y+2
    if( (direction == "n") ):
        if(x-2 >= 0):
            return x-2,y
    if( (direction == "w") ):
        if(y-2 >= 0):
            return x,y-2


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


def bfs(cur_state,point_table):
    frontier_list = ["flag"]
    counter = 0
    root_bfs = Node(cur_state)

    while frontier_list:
        if(frontier_list[0] == "flag"):
            frontier_list.pop(0)
        #print("Counter: ",counter)
        print("Current State: \n",cur_state)
        #print("type of cur_state: ",type(cur_state))
        parent_state = cur_state
        move_list = list_possible_moves(cur_state)
        for new_states in move_list:
            peg_x = int(new_states[0])
            peg_y = int(new_states[1])
            way = new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            #print("\n:::\nmove value: ",move_value,"\n:::\n")
            new_state = board.make_move(np.copy(cur_state),peg_x,peg_y,way)
            Node(new_state,parent=parent_state)
            frontier_list.append((move_value,new_state))
        if frontier_list:
            cur_fr_list_element = frontier_list.pop(0)
            cur_state = cur_fr_list_element[1]
            if(np.array_equal(cur_state,SOLUTION)):
                print("AWESOME")
                return True
        else:
            print("DONE")
            cur_state = None
            return True
        #print("New Frontier List:\n",frontier_list)
        if (frontier_list):
            bfs(cur_state,point_table)
        counter +=1
    #print("BFS DONE COUNT: ",counter)
    return True
    #for x in range(len(move_list)):



def dfs(cur_state,point_table):
    frontier_list = [("flag",cur_state)]
    counter = 0
    while frontier_list:
        if frontier_list[0] =="flag":
            frontier_list.pop(0)
        print("Sıra: ",counter)
        move_list = list_possible_moves(cur_state)
        move_list.sort(reverse=True)
        for new_states in move_list:
            peg_x = int(new_states[0])
            peg_y = int(new_states[1])
            way = new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            #print("\n:::\nmove value: ",move_value,"\n:::\n")
            new_state = board.make_move(np.copy(cur_state),peg_x,peg_y,way)
            #print("New State:\n",new_state)
            frontier_list.append((move_value,new_state))
        #print("Sorted Frontier List:\n",frontier_list)
        if frontier_list:
            last_element = len(frontier_list)
            cur_fr_list_element = frontier_list.pop(last_element-1)
            cur_state = cur_fr_list_element[1]
            """
            if(np.array_equal(cur_state,SAMPLE)):
                print("THAT'S GOOD")
                return True
            """
            if(np.array_equal(cur_state,SOLUTION)):
                print("AWESOME")
                return True
        else:
            print("DONE")
            cur_state = None
            return True
        #print("New Frontier List:\n",frontier_list)
        #if (frontier_list):
        #    dfs(cur_state,point_table)
        counter +=1
    print("Count: ",counter)
    #7667769. sırada sonuç buldu #TODO
    
    #for x in range(len(move_list)):