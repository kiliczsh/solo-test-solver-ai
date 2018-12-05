class MyNode:
    def __init__(self, board, parent,depth_level,peg_number):
        self.parent = parent
        self.board = board
        self.depth_level = depth_level
        self.peg_number = peg_number
    
    def info(self):
        print("\nNode Board: \n",self.board," \n\nParent Node: \n",self.parent,"\n")

    