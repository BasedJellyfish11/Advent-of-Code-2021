from collections import defaultdict, deque, namedtuple
from pprint import pprint

test = False

def parse():
    with open(f"../input/{'test_' if test else ''}day12.txt") as f:
        lines = [x.strip() for x in f.readlines()]

    graph = defaultdict(set)

    for line in lines:
        start, end = line.split("-")

        graph[start].add(end)
        graph[end].add(start)

    for v in graph.values():
        v -= {'start'}

    del graph['end']

    smalls = set(x for x in graph if x == x.lower())

    return graph, smalls


def bfs(graph, smalls, allow_multi=False):
    q = deque([
            (
                "start",
                set(),
                False,
            )
    ])

    fin = 0

    while q:
        node, visited, small_twice = q.pop()

        if node == "end":
            fin += 1
            continue

        for adj in graph[node]:
            visited_adj = adj in visited

            if visited_adj and (small_twice or not allow_multi):
                continue

            new_visited = visited

            if adj in smalls:
                # not += because that's in-place.
                new_visited = new_visited | { adj }

            q.append(
                (
                    adj,
                    new_visited,
                    small_twice or visited_adj,
                )
            )

    pprint(fin)


if __name__ == "__main__":
    parsed = parse()
    bfs(*parsed)
    bfs(*parsed, True)
