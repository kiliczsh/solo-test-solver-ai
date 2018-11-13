import numpy as np


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
    
    def update_board(self):
        for i in range(len(self.board_array)):
            for j in range(len(self.board_array[i])):
                if self.board_array[i, j] == '*':
                    self.board_array[i, j] = 0
                elif self.board_array[i, j] == 'o':
                    self.board_array[i, j] = 1
                else:
                    self.board_array[i, j] = 2
       


# ------------------------------------------  main method -----------------------------------------
if __name__ == "__main__":

    game_board = Board()
    game_board.update_board()
    game_board.print_board()
    


