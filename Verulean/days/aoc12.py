from collections import defaultdict


class CavePaths:
    def __init__(self, data):
        data = [pair.split('-') for pair in data]
        
        # Parse data into connection dictionary
        self._connections = defaultdict(set)
        for a, b in data:
            self._connections[a].add(b)
            self._connections[b].add(a)
        
        del self._connections['end']
        for options in self._connections.values():
            options -= {'start',}
        
        # Intiialize other instance variables
        self._completed_paths = set()
        self._small = set(cave for cave in self._connections if cave == cave.lower())
        
    def _routes(self, path, small_validator):
        for cave in self._connections[path[-1]]:
            if cave in self._small and cave in path:
                if small_validator(path):
                    yield cave
            else:
                yield cave
    
    def _count_paths(self, part):
        self._completed_paths.clear()
        
        if part == 1:
            def validator(path):
                return False
        elif part == 2:
            def validator(path):
                for small_cave in self._small:
                    if path.count(small_cave) >= 2:
                        return False
                return True
        
        paths = {('start',),}
        while paths:
            old_paths, paths = paths, set()
            for path in old_paths:
                if path[-1] == 'end':
                    self._completed_paths.add(path)
                else:
                    for next_cave in self._routes(path, validator):
                        paths.add(path + (next_cave,))

        return len(self._completed_paths)
    
    def solve(self):
        return tuple(self._count_paths(part) for part in (1, 2))

def solve(data):
    return CavePaths(data).solve()