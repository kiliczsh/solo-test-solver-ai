import numpy as np

LIMIT = 7

DIRECTION = ['n', 'e', 's', 'w']

INITIAL = np.array([[2, 2, 1, 1, 1, 2, 2],
                   [2, 2, 1, 1, 1, 2, 2],
                   [1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 0, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1],
                   [2, 2, 1, 1, 1, 2, 2],
                   [2, 2, 1, 1, 1, 2, 2]],dtype=np.int)

SOLUTION = np.array([[2, 2, 0, 0, 0, 2, 2],
                     [2, 2, 0, 0, 0, 2, 2],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [2, 2, 0, 0, 0, 2, 2],
                     [2, 2, 0, 0, 0, 2, 2]])


POINT_TABLE = np.array([[999, 999,   1,   2,   3, 999, 999],
                        [999, 999,   4,   5,   6, 999, 999],
                        [  7,   8,   9,  10,  11,  12,  13],
                        [ 14,  15,  16,  17,  18,  19,  20],
                        [ 21,  22,  23,  24,  25,  26,  27],
                        [999, 999,  28,  29,  30, 999, 999],
                        [999, 999,  31,  32,  33, 999, 999]])
# comparison of np.arrays
def is_equal(arr_1,arr_2):
    if(np.array_equal(arr_1,arr_2)):
        return True
    else:
        return False

# returns new coordinates of peg moved
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

# get depth of a solution
def count_depth(new_node):
    depth_level = 0
    parent_node = new_node.parent
    while(parent_node != None):
        depth_level += 1
        parent_node = parent_node.parent
    return depth_level

#get number of pegs on current solution
def count_pegs(new_node):
    board = new_node.board
    peg_count = 0
    for i in range(LIMIT):
        for j in range(LIMIT):
            sqr = int(board[i][j])
            IS_PEG = (sqr == 1)
            if(IS_PEG):
                peg_count += 1
    return peg_count
                