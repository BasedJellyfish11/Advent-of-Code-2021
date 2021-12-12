from collections import defaultdict, deque, namedtuple
from pprint import pprint

Search = namedtuple("Search", ["node", "path", "visited", "twice"])

test = False

def parse():
    with open(f"../input/{'test_' if test else ''}day12.txt") as f:
        lines = [x.strip() for x in f.readlines()]

    graph = defaultdict(set)

    for line in lines:
        start, end = line.split("-")

        graph[start].add(end)
        graph[end].add(start)

    smalls = set(x for x in graph if x == x.lower())

    return graph, smalls


def bfs(graph, smalls, allow_multi=False):
    q = deque([
            Search(
                node="start",
                path=("start",),
                visited={"start"},
                twice=False,
            )
    ])

    fin = set()

    while q:
        node, path, visited, small_twice = q.pop()

        if node == "end":
            fin.add(path)
            continue

        for adj in graph[node]:
            if adj == "start":
                continue

            visited_adj = adj in visited

            if visited_adj and (small_twice or not allow_multi):
                continue

            new_visited = visited

            if adj in smalls:
                # not += because that's in-place.
                new_visited = new_visited | { adj }

            q.append(
                Search(
                    node=adj,
                    path=path + (adj,),
                    visited=new_visited,
                    twice=small_twice or visited_adj,
                )
            )

    if test:
        pprint(fin)

    pprint(len(fin))


if __name__ == "__main__":
    parsed = parse()
    bfs(*parsed)
    bfs(*parsed, True)
