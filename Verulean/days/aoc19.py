from collections import defaultdict


fmt_dict = {
    'sep': '\n\n'
    }

axis_rotations = (
    ((0,1,2), (1,1,1)),
    ((0,1,2), (1,-1,-1)),
    ((0,1,2), (-1,1,-1)),
    ((0,1,2), (-1,-1,1)),
    ((1,2,0), (1,1,1)),
    ((1,2,0), (1,-1,-1)),
    ((1,2,0), (-1,1,-1)),
    ((1,2,0), (-1,-1,1)),
    ((2,0,1), (1,1,1)),
    ((2,0,1), (1,-1,-1)),
    ((2,0,1), (-1,1,-1)),
    ((2,0,1), (-1,-1,1)),
    ((0,2,1), (-1,-1,-1)),
    ((0,2,1), (1,1,-1)),
    ((0,2,1), (1,-1,1)),
    ((0,2,1), (-1,1,1)),
    ((1,0,2), (-1,-1,-1)),
    ((1,0,2), (1,1,-1)),
    ((1,0,2), (1,-1,1)),
    ((1,0,2), (-1,1,1)),
    ((2,1,0), (-1,-1,-1)),
    ((2,1,0), (1,1,-1)),
    ((2,1,0), (1,-1,1)),
    ((2,1,0), (-1,1,1)),
    )

class Point3D(tuple):
    def __neg__(self):
        return type(self)(-x for x in self)
    
    def __sub__(self, other):
        return type(self)(s-o for s, o in zip(self, other))
    
    def __rsub__(self, other):
        return -self + other
    
    def __add__(self, other):
        return type(self)(s+o for s, o in zip(self, other))
    
    def __radd__(self, other):
        return self + other
    
    def __mul__(self, other):
        return type(self)(s*o for s, o in zip(self, other))
    
    def __rmul__(self, other):
        return self * other
    
    def __abs__(self):
        return type(self)(abs(s) for s in self)
    
    def permute(self, p):
        return type(self)(self[i] for i in p)

def parse_scanner(data):
    data = data.split('\n')[1:]
    points = {Point3D(int(x) for x in point.split(',')) for point in data}
    
    snowflake = defaultdict(set)
    for root in points:
        for other in points - {root}:
            snowflake[root].add(other - root)
    
    return points, snowflake

def rotate_points(points, permutation, reflection):
    return {reflection * point.permute(permutation) for point in points}

def rotate_snowflake(snowflake, permutation, reflection):
    new_flake = {}
    for root, offsets in snowflake.items():
        new_root = reflection * root.permute(permutation)
        new_flake[new_root] = rotate_points(offsets, permutation, reflection)
    return new_flake

def shift_points(points, shift):
    return {point+shift for point in points}

def find_shift(snow1, snow2, required=12):
    for target, rel1 in snow1.items():
        for source, rel2 in snow2.items():
            if len(rel1 & rel2) >= required - 1:
                return target - source
    return False

def find_map(A, B):
    for i, B_rot in enumerate(B):
        shift = find_shift(A, B_rot)
        if shift:
            return *axis_rotations[i], shift
    return False

def forward_map(point, p, r, s):
    return r * Point3D(point).permute(p) + s

def reverse_map(point, p, r, s):
    new_point = [0, 0, 0]
    for i, (refl, shift) in enumerate(zip(r, s)):
        new_point[p[i]] = refl * (point[i] - shift)
    return Point3D(new_point)

def map_points(points, map_key):
    direction, point_map = map_key
    if direction == 0:
        return {forward_map(point, *point_map) for point in points}
    elif direction == 1:
        return {reverse_map(point, *point_map) for point in points}

def build_maps(snowflakes):
    maps = {}
    N = len(snowflakes)
    for i in range(N):
        for j in range(i+1, N):
            if (m := find_map(snowflakes[i][0], snowflakes[j])):
                maps[(i, j)] = (0, m)
                maps[(j, i)] = (1, m)
    return maps

def reassembly_order(maps, scanners):
    to_cover = set(scanners)
    covered = set()
    
    pools = defaultdict(set)
    for target, source in maps.keys():
        pools[target].add(source)
    
    order = []
    final_target = max(pools.items(), key=lambda x: len(x[1]))[0]
    covered |= pools[final_target] | {final_target}
    order.append((pools[final_target], final_target))
    del pools[final_target]
    
    while covered != to_cover:
        target = max((t for t in pools.items() if t[0] in covered), key=lambda x: len(x[1]))[0]
        if new_sources := pools[target] - covered:
            order.append((new_sources, target))
        covered |= pools[target]
        del pools[target]
    
    return final_target, order

def max_manhattan(points):
    points = tuple(points)
    m = 0
    for ia, a in enumerate(points):
        for b in points[ia+1:]:
            m = max(m, sum(abs(a-b)))
    return m

def solve(data):
    N = len(data)
    scanners = []
    snowflakes = []
    
    for i, scanner in enumerate(data):
        points, snowflake = parse_scanner(scanner)
        scanners.append(points)
        snowflakes.append([snowflake])
    
    for i in range(N):
        for j in range(1, len(axis_rotations)):
            snowflakes[i].append(rotate_snowflake(snowflakes[i][0], *axis_rotations[j]))
    
    maps = build_maps(snowflakes)
    final_scanner, order = reassembly_order(maps, range(N))
    
    scanner_positions = {i:{(0,0,0)} for i, _ in enumerate(scanners)}
    beacon_builder = {i:points for i, points in enumerate(scanners)}
    
    for sources, target in reversed(order):
        for source in sources:
            beacon_builder[target] |= map_points(beacon_builder[source], maps[(target, source)])
            scanner_positions[target] |= map_points(scanner_positions[source], maps[(target, source)])
    
    beacon_count = len(beacon_builder[final_scanner])
    scanner_positions = scanner_positions[final_scanner]
    return beacon_count, max_manhattan(scanner_positions)