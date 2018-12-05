import numpy as np
import path 

LIMIT = 7


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
    
    # print board properly
    def print_board(self):
        print("\n 0  | ",end="")
        for i in range(LIMIT):
            for j in range(LIMIT):
                print(self.board_array[i][j],end=" ")
            print("\n",i+1," | ",end="")
        print()
    # end of printing board array
    
    # give each square points in document
    def create_square_points(self):
        s = (LIMIT,LIMIT)
        point_array = np.zeros(s,dtype=np.int)
        counter = 0
        for i in range(LIMIT):
            for j in range(LIMIT):
                cur_val = int(self.board_array[i, j])
                if ((cur_val is 1) or (cur_val is 0)):
                    counter += 1
                    ass_num = counter
                else:
                    ass_num = 999
                point_array[i,j] = ass_num
        print(point_array)
        print()
        return point_array
    # end of function


    # check whether is the solution is optimum
    def check_win(self):
        flag = True
        for i in range(LIMIT):
            for j in range(LIMIT):
                num = int(self.board_array[i,j])
                
                if( (i==0 or i==1 or i==5 or i==6) & (j==0 or j==1 or j==5 or j==6) ):
                    if(not num == 2):
                        flag = False
                elif( i==3 and j==3 ):
                    if(not num == 1):
                        flag = False
                else:
                    if(not num == 0):
                        flag = False
        return flag
        
    # uses game1 in path module and plays it
    def play_game(self):
        game_path = path.Path()
        game1 = game_path.game1() #TODO
        for mov in game1:
            self.make_move(mov[0],mov[1],mov[2])
    


                    