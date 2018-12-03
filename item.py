import numpy as np

LIMIT = 7

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
