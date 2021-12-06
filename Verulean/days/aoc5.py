import numpy as np


def count_overlaps(*grids):
    return tuple(np.sum(grid >= 2) for grid in grids)

def solve(x):
    coords = np.array([[coord.split(',') for coord in line.split(' -> ')] for line in x], dtype=int)
    deltas = coords[:,1] - coords[:,0]
    signs = np.where(deltas >= 0, 1, -1)
    
    grid = np.zeros((2, *np.amax(coords, axis=(0,2))+1), dtype=int)
    for c, d, s in zip(coords, deltas, signs):
        grid[int(np.all(d!=0))][tuple(c[0,i]+np.arange(0,d[i]+s[i],s[i]) for i in range(2))] += 1

    return count_overlaps(grid[0], grid[0]+grid[1])