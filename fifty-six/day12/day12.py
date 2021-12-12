from collections import defaultdict, deque
from pprint import pprint

test = False

with open(f"../input/{'test_' if test else ''}day12.txt") as f:
    lines = [x.strip() for x in f.readlines()]

graph = defaultdict(set)

smalls = set()

for line in lines:
    start, end = line.split("-")

    graph[start].add(end)
    graph[end].add(start)

    # yeah it's inefficient what about it
    if start.lower() == start:
        smalls.add(start)
    if end.lower() == end:
        smalls.add(end)


def bfs(allow_multi=False):
    # tuple of (node, path, visited_smalls, has_visited_small_twice)
    q = deque([("start", ("start",), {"start": 2}, False)])

    fin = set()

    while q:
        node, path, visited, small_twice = q.pop()

        if node == "end":
            fin.add(path)
            continue

        for adj in graph[node]:
            if adj == "start":
                continue

            visit_count = visited.get(adj, 0)

            if visit_count >= 1 and (small_twice or not allow_multi):
                continue

            new_visited = visited

            if adj in smalls:
                # not += because that's in-place.
                new_visited = new_visited | {adj: visit_count + 1}

            q.append((adj, path + (adj,), new_visited, small_twice or visit_count >= 1))

    if test:
        pprint(fin)
    pprint(len(fin))


bfs()
bfs(True)
