import numpy as np

def man_dist(board_array):
    dist = 0
    peg_count = 0
    for i in range(len(board_array)):
        for j in range(len(board_array)):
            if (int(board_array[i, j]) == 1):
                peg_count += 1
                for k in range(len(board_array)):
                    for l in range(len(board_array)):
                        if (int(board_array[k, l]) == 1):
                            dist += abs(i - k) + abs(j - l)
    ret_val = dist / (2 * peg_count)
    return ret_val

#def calc(board_array):

