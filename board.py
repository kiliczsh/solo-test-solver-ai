import numpy as np
import path 

class Board:

    def __init__(self,directions,board_array):
        self.directions = directions
        self.board_array = board_array
    
    # print board properly
    def print_board(self):
        print("\n 0  | ",end="")
        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[i])):
                print(self.board_array[i][j],end=" ")
            print("\n",i+1," | ",end="")
        print()
    # end of printing board array
    
    # change board array with numeric values
    def update_board(self):
        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[i])):
                if self.board_array[i, j] == '*':
                    self.board_array[i, j] = 1
                elif self.board_array[i, j] == 'o':
                    self.board_array[i, j] = 0
                else:
                    self.board_array[i, j] = 2
    # end of board

    # make moves with given coordinates and directions
    def make_move(self,board_array_param,x,y,direction):
        counter = 0
        #print(board_array_param)
        if( (x==0 or x==1 or x==5 or x==6) & (y==0 or y==1 or y==5 or y==6) ):
            return board_array_param
        for i in range(len(board_array_param)):
            for j in range(len(board_array_param[i])):
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

    # check whether is the solution is optimum
    def check_win(self):
        flag = True
        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[i])):
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
    
    def list_possible_moves(self,board_array_param):
        fun_move_list = []
        for i in range(len(board_array_param)):
            for j in range(len(board_array_param[i])):
                current_square = int(board_array_param[i,j])
                bannned_square = (i==0 or i==1 or i==5 or i==6) and (j==0 or j==1 or j==5 or j==6)
                if(not bannned_square):
                    if(current_square == 1):
                        try:
                            right_square = None
                            if(j+2 < 7 ):
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
                            if(i+2 < 7):
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

                    