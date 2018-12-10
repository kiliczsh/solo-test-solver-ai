import numpy as np
from item import LIMIT

# make moves with given coordinates and directions
def make_move(board_array_param,x,y,direction):
    counter = 0
    #print(board_array_param)
    if( (x==0 or x==1 or x==5 or x==6) & (y==0 or y==1 or y==5 or y==6) ):
        return board_array_param
    for i in range(LIMIT):
        for j in range(LIMIT):
            if( (x is i) and (y is j) ):
                board_array_param[i,j] = 0
                if( (direction == "s") ):
                    board_array_param[i+2,j] = 1
                    board_array_param[i+1,j] = 0
                if( (direction == "e") ):
                    board_array_param[i,j+2] = 1
                    board_array_param[i,j+1] = 0
                if( (direction == "n") ):
                    board_array_param[i-2,j] = 1
                    board_array_param[i-1,j] = 0
                if( (direction == "w") ):
                    board_array_param[i,j-2] = 1
                    board_array_param[i,j-1] = 0
            else:       
                counter += 1
    #print(board_array_param)
    return board_array_param


class Board:

    def __init__(self,directions,board_array):
        self.directions = directions
        self.board_array = board_array
    



                    