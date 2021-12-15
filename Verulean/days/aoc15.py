import numpy as np


def neighbors(i, j, m, n):
    candidates = ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
    for ii, jj in candidates:
        if 0 <= ii < m and 0 <= jj < n:
            yield ii, jj

# The classic O((mn)^2) time complexity
def numpy_dijkstra(costs):
    m, n = costs.shape
    
    visited = np.zeros_like(costs, dtype=bool)
    distance = np.full_like(costs, np.inf)
    distance[0, 0] = 0
    
    i, j = 0, 0
    while not visited[-1, -1]:
        visited[i, j] = True
        for ii, jj in neighbors(i, j, m, n):
            distance[ii, jj] = min(
                distance[ii, jj], 
                distance[i, j] + costs[ii, jj]
                )
        i, j = np.unravel_index(
            np.argmin(
                np.where(
                    ~visited, 
                    distance, 
                    np.inf
                    )
                ), 
            distance.shape
            )
    
    return int(distance[-1, -1])

def expand_block(block, M, N):
    m, n = block.shape
    
    shift = np.add.outer(np.arange(M), np.arange(N), dtype=float)
    shift = np.repeat(np.repeat(shift, m, axis=0), n, axis=1)
    
    new_block = ((np.tile(block, (M, N)) + shift - 1) % 9) + 1
    
    return new_block

def solve(data):
    costs_a = np.array([list(row) for row in data], dtype=float)
    ans_a = numpy_dijkstra(costs_a)
    
    costs_b = expand_block(costs_a, 5, 5)
    ans_b = numpy_dijkstra(costs_b)
    
    return ans_a, ans_b