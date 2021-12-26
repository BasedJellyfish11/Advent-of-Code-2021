import numpy as np
import heapq


class PriorityQueue(list):
    def pop(self):
        return heapq.heappop(self)
    def push(self, value):
        return heapq.heappush(self, value)

def neighbors(i, j, m, n):
    candidates = ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
    for ii, jj in candidates:
        if 0 <= ii < m and 0 <= jj < n:
            yield ii, jj

def numpy_dijkstra(costs):
    m, n = costs.shape
    
    start = (0, 0)
    end = (m - 1, n - 1)
    
    q = PriorityQueue()
    q.push((0, start))
    
    g = np.full_like(costs, np.inf)
    g[start] = 0
    
    while q:
        cost, (i, j) = q.pop()
        if (i, j) == end:
            return int(g[end])
        
        for adj in neighbors(i, j, m, n):
            adj_cost = cost + costs[adj]
            if adj_cost < g[adj]:
                g[adj] = adj_cost
                q.push((adj_cost, adj))

def expand_block(block, M, N):
    m, n = block.shape
    
    shift = np.add.outer(np.arange(M), np.arange(N))
    shift = np.repeat(np.repeat(shift, m, axis=0), n, axis=1)
    
    new_block = ((np.tile(block, (M, N)) + shift - 1) % 9) + 1
    
    return new_block

def solve(data):
    costs_a = np.array([list(row) for row in data], dtype=float)
    ans_a = numpy_dijkstra(costs_a)
    
    costs_b = expand_block(costs_a, 5, 5)
    ans_b = numpy_dijkstra(costs_b)
    
    return ans_a, ans_b