class MyNode:
    def __init__(self, board, parent):
        self.parent = parent
        self.board = board
    
    def info(self):
        print("\nNode Board: \n",self.board," \n\nParent Node: \n",self.parent,"\n")

    