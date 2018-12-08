import numpy as np

def man_dist(board_array):
    dist = 0
    peg_count = 0
    ret_val = 999
    if(not is_crying(np.copy(board_array))):
        for i in range(len(board_array)):
            for j in range(len(board_array)):
                if (int(board_array[i, j]) == 1):
                    peg_count += 1
                    for k in range(len(board_array)):
                        for l in range(len(board_array)):
                            if (int(board_array[k, l]) == 1):
                                dist += abs(i - k) + abs(j - l)
        ret_val = dist / (2 * peg_count)
    else:
        ret_val = 999
    return ret_val

def is_crying(board_array):
    for i in range(len(board_array)):
        for j in range(len(board_array)):
            IS_BAN = (i==0 or i==1 or i==5 or i==6) and (j==0 or j==1 or j==5 or j==6)
            IS_EDGE = (i==0 or i==6 or j==0 or j==6)  
            if(not IS_BAN):
                cur_sqr = int(board_array[i, j])
                if(not IS_EDGE):
                    left = int(board_array[i, j-1])
                    right = int(board_array[i, j+1])
                    up = int(board_array[i-1, j])
                    down = int(board_array[i+1, j])
                else:
                    if(i==0): 
                        up = 3 
                        left = int(board_array[i, j-1])
                        right = int(board_array[i, j+1])
                        down = int(board_array[i+1, j])
                    if(i==6): 
                        down = 3
                        left = int(board_array[i, j-1])
                        right = int(board_array[i, j+1])
                        up = int(board_array[i-1, j])
                    if(j==0): 
                        left = 3
                        right = int(board_array[i, j+1])
                        up = int(board_array[i-1, j])
                        down = int(board_array[i+1, j])
                    if(j==6): 
                        right = 3
                        up = int(board_array[i-1, j])
                        down = int(board_array[i+1, j])
                        left = int(board_array[i, j-1])
                if(cur_sqr == 1):
                    if(left != 1 and right!=1 and up!=1 and down!=1): 
                        return True


                




