import numpy as np 
import board
import heuristic as heu
"""


def create_and_add(acker,prev_board,move_list):
    for x in range(len(move_list)):
        next_board = game_board.make_move(np.copy(prev_board),move_list[x][0],move_list[x][1],move_list[x][2] )
        #print("\nBoard Man: ",heuristic.man_dist(next_board),"\n\n")
        Node(next_board,parent=acker)
    return acker


"""







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




def bfs(cur_state,point_table):
    frontier_list = ["flag"]

    while frontier_list:
        if(frontier_list[0]=="flag"):
            frontier_list.pop(0)
        print("lis")
        move_list = board.Board.list_possible_moves(0,cur_state)

        for new_states in move_list:
            peg_x = int(new_states[0])
            peg_y = int(new_states[1])
            way = new_states[2]
            free_x,free_y = get_extra(peg_x,peg_y,way)
            move_value = int(point_table[peg_x,peg_y]) + int(point_table[free_x,free_y])
            frontier_list.append((move_value,new_states))
        frontier_list.sort()
        print(frontier_list)
        cur_state = frontier_list.pop(0)
        bfs(cur_state)
    
        
    #for x in range(len(move_list)):



