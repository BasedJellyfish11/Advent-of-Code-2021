import numpy as np
from collections import defaultdict


def all_done(paths):
    for path in paths:
        if path[-1] != 'end':
            return False
    return True

PART = 2

def solve(data):
    paths = set()
    data = [line.split('-') for line in data]
    
    data = [(s, e) for s, e in data] \
        + [(e, s) for s, e in data]
    
    ways = defaultdict(list)
    for start, end in data:
        if start != 'end' and end != 'start':
            ways[start] += [end]
    
    
    caves = set(ways.keys())
    big = set([cave for cave in caves if cave == cave.upper()])
    
    small = list(caves - big)
    
    def can_fit_extra_small(path):
        for cave in small:
            if path.count(cave) > 1:
                return False
        return True
    
    def options(path):
        for cave in ways[path[-1]]:
            if cave in path and cave in small:
                if PART == 2 and can_fit_extra_small(path):
                    yield cave
                continue
            yield cave
    
    
    paths = {('start',),}
    
    while not all_done(paths):
        new_paths = set()
        for path in list(paths):
            if o := list(options(path)):
                for next_cave in o:
                    # print(path, next_cave)
                    new_paths.add(tuple(path + (next_cave,)))
            elif path[-1] == 'end':
                new_paths.add(path)
            paths = new_paths
    
    return 'ANSWER', len(paths)