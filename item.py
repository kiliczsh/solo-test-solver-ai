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


SAMPLE = np.array([[2, 2, 0, 1, 1, 2, 2],
                   [2, 2, 0, 0, 1, 2, 2],
                   [1, 0, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1],
                   [2, 2, 1, 1, 1, 2, 2],
                   [2, 2, 1, 1, 1, 2, 2]])

POINT_TABLE = np.array([[999, 999,   1,   2,   3, 999, 999],
                        [999, 999,   4,   5,   6, 999, 999],
                        [  7,   8,   9,  10,  11,  12,  13],
                        [ 14,  15,  16,  17,  18,  19,  20],
                        [ 21,  22,  23,  24,  25,  26,  27],
                        [999, 999,  28,  29,  30, 999, 999],
                        [999, 999,  31,  32,  33, 999, 999]])

MY_POINT_TABLE = np.array([[999, 999,   1,   2,   3, 999, 999],
                           [999, 999,  13,  14,  15, 999, 999],
                           [ 12,  24,  25,  26,  27,  16,   4],
                           [ 11,  23,  32,  33,  28,  17,   5],
                           [ 10,  22,  31,  30,  29,  18,   6],
                           [999, 999,  21,  20,  19, 999, 999],
                           [999, 999,   9,   8,   7, 999, 999]])

MY_POINT_TABLE_TWO = np.array([[999, 999,   1,   2,   3, 999, 999],
                               [999, 999,  25,  29,   4, 999, 999],
                               [ 21,  22,  23,  24,   5,  26,   7],
                               [ 20,  32,  18,  33,   6,  30,   8],
                               [ 19,  28,  17,  12,  11,  10,   9],
                               [999, 999,  16,  31,  27, 999, 999],
                               [999, 999,  15,  14,  13, 999, 999]])

def is_equal(arr_1,arr_2):
    if(np.array_equal(arr_1,arr_2)):
        return True
    else:
        return False

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


def count_depth(new_node):
    depth_level = 0
    parent_node = new_node.parent
    while(parent_node != None):
        depth_level += 1
        parent_node = parent_node.parent
    return depth_level

def count_pegs(new_node):
    board = new_node.board
    peg_count = 0
    for i in range(LIMIT):
        for j in range(LIMIT):
            sqr = int(board[i][j])
            IS_PEG = not((sqr != 0) and (sqr != 2))
            if(IS_PEG):
                peg_count += 1
    return peg_count
                