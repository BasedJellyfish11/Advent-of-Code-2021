import numpy as np


def step(cucs):
    moved = False
    can_move_east = np.roll(cucs[0], 1, axis=1) & (~ cucs[1]) & (~cucs[0])
    if np.any(can_move_east):
        moved = True
        cucs[0] |= can_move_east
        cucs[0] ^= np.roll(can_move_east, -1, axis=1)
    
    can_move_south = np.roll(cucs[1], 1, axis=0) & (~ cucs[0]) & (~cucs[1])
    if np.any(can_move_south):
        moved = True
        cucs[1] |= can_move_south
        cucs[1] ^= np.roll(can_move_south, -1, axis=0)
    
    return moved


def solve(data):
    data = np.array([list(line) for line in data])
    m, n = data.shape
    cucs = np.zeros((2, m, n), dtype=bool)
    # 0 -> East, 1 -> South
    cucs[0] = np.where(data == '>', True, False)
    cucs[1] = np.where(data == 'v', True, False)
    
    s = 1
    while step(cucs):
        s+= 1
    
    return s