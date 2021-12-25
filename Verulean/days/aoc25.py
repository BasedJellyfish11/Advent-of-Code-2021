import numpy as np


def step(east_herd, south_herd):
    move_east = np.roll(east_herd, 1, axis=1) & ~(east_herd | south_herd)
    east_herd ^= (move_east | np.roll(move_east, -1, axis=1))
    
    move_south = np.roll(south_herd, 1, axis=0) & ~(east_herd | south_herd)
    south_herd ^= (move_south | np.roll(move_south, -1, axis=0))
    
    return np.any(move_east | move_south)

def solve(data):
    data = np.array([list(row) for row in data])
    
    east_herd = (data == '>')
    south_herd = (data == 'v')
    
    step_count = 1
    while step(east_herd, south_herd):
        step_count += 1
    
    return step_count