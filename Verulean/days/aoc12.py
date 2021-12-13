from collections import defaultdict, deque


class CavePaths:
    def __init__(self, data):
        data = [pair.split('-') for pair in data]
        
        # Parse data into connection dictionary
        self._connections = defaultdict(set)
        for a, b in data:
            self._connections[a].add(b)
            self._connections[b].add(a)
        
        # Cannot leave end or re-enter start
        del self._connections['end']
        for options in self._connections.values():
            options -= {'start'}
        
        # Identify small caves
        self._small = set(cave for cave in self._connections if cave.islower())
    
    def _count_paths(self, allow_multi=False):
        completed_paths = 0
        
        paths = deque([(
                "start",
                {"start"},
                False,
                )])
        
        while paths:
            node, visited, small_twice = paths.pop()
            
            if node == 'end':
                completed_paths += 1
                continue

            for next_cave in self._connections[node]:
                revisit = next_cave in visited
                if revisit and (small_twice or not allow_multi):
                    continue
                
                new_visited = \
                    visited | {next_cave} \
                    if next_cave in self._small \
                    else visited
                
                paths.append((next_cave, new_visited, small_twice or revisit))

        return completed_paths
    
    def solve(self):
        return self._count_paths(), self._count_paths(True)

def solve(data):
    return CavePaths(data).solve()