from functools import lru_cache
from pprint import pprint
from collections import deque
import heapq

def parse():
    test = False
    
    with open(f"../input/{'test_' if test else ''}day15.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    
    return [[int(x) for x in y] for y in lines]

def in_bounds(h, length):
    return 0 <= h[0] < length and 0 <= h[1] < length

class PriorityQueue:
    def __init__(self, iterable=[]):
        self.queue: List = list(iterable)

    def __iter__(self):
        return iter(self.queue)

    def __bool__(self):
        return bool(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    # It's faster to just heapdown.
    # noinspection PyProtectedMember
    def remove(self, index):
        self.queue[index] = self.queue[-1]
        del self.queue[-1]

        heapq._siftdown(self.queue, index, 0)

    def pop(self):
        return heapq.heappop(self.queue)

    def push(self, value):
        return heapq.heappush(self.queue, value)

    def peek(self):
        return self.queue[0]

def heuristic(a, b):
    return abs(b[1] - a[1]) + abs(b[0] - a[0])

def search(grid):
    length = len(grid)

    start = (0, 0)
    end = (length - 1, length - 1)

    q = PriorityQueue()
    q.push((heuristic(start, end), 0, start))

    costs = { start: heuristic(start, end) }

    while q:
        _, cost, node = q.pop()

        if node == end:
            return cost

        x, y = node

        for adj in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if not in_bounds(adj, length):
                continue

            ax, ay = adj

            a_cost = cost + grid[ax][ay]
            heur = a_cost + heuristic(adj, end)

            if heur < costs.get(adj, float('inf')):
                costs[adj] = heur
                q.push((heur, a_cost, adj))

def clamp(v, u):
    return v if  v <= u else v % u

def solve(grid):
    new_grid = [[0] * len(grid) * 5 for _ in range(len(grid) * 5)]

    orig_len = len(grid)

    for i, r in enumerate(grid):
        for j, v in enumerate(r):
            for k in range(5):
                for l in range(5):
                    new_grid[i + orig_len * k][j + orig_len * l] = clamp(v + k + l, 9)

    print(search(grid))
    print(search(new_grid))

if __name__ == "__main__":
    solve(parse())
