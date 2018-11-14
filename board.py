import numpy as np
import path 

class Board:
    directions = ['n', 'e', 's', 'w']
    board_array = np.array([[".", ".", "*", "*", "*", ".", "."],
                            [".", ".", "*", "*", "*", ".", "."],
                            ["*", "*", "*", "*", "*", "*", "*"],
                            ["*", "*", "*", "o", "*", "*", "*"],
                            ["*", "*", "*", "*", "*", "*", "*"],
                            [".", ".", "*", "*", "*", ".", "."],
                            [".", ".", "*", "*", "*", ".", "."]])
    
    # print board properly
    def print_board(self):
        print()
        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[i])):
                print(self.board_array[i][j],end=" ")
            print("\n")
    # end of printing board array
    
    # change board array with numeric values
    def update_board(self):
        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[i])):
                if self.board_array[i, j] == '*':
                    self.board_array[i, j] = 0
                elif self.board_array[i, j] == 'o':
                    self.board_array[i, j] = 1
                else:
                    self.board_array[i, j] = 2
    # end of board

    # make moves with given coordinates and directions
    def make_move(self,x,y,direction):
        counter = 0
        if( (x==0 or x==1 or x==5 or x==6) & (y==0 or y==1 or y==5 or y==6) ):
            return self.board_array
        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[i])):
                if( (x is i) and (y is j) ):
                    self.board_array[i,j] = 1
                    if( (direction == "s") ):
                        self.board_array[i+2,j] = 0
                        self.board_array[i+1,j] = 1
                    if( (direction == "e") ):
                        self.board_array[i,j+2] = 0
                        self.board_array[i,j+1] = 1
                    if( (direction == "n") ):
                        self.board_array[i-2,j] = 0
                        self.board_array[i-1,j] = 1
                    if( (direction == "w") ):
                        self.board_array[i,j-2] = 0
                        self.board_array[i,j-1] = 1
                else:
                    counter += 1
        return self.board_array

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
                    if(not num == 0):
                        flag = False
                else:
                    if(not num == 1):
                        flag = False
        return flag
        
    # uses game1 in path module and plays it
    def play_game(self):
        game_path = path.Path()
        game1 = game_path.game1() #TODO
        for mov in game1:
            self.make_move(mov[0],mov[1],mov[2])

                    
                    
                    
                