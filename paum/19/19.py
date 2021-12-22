scanners = []

for s in scanners:
    print(s)

def get_oriented_tuple(tup, orientation):
    orient_div = orientation // 4
    root_div = orientation % 4
    if orient_div == 0:
        inter_tup = (tup[0], tup[1], tup[2])
    elif orient_div == 1:
        inter_tup = (-1 * tup[0], tup[2], tup[1])
    elif orient_div == 2:
        inter_tup = (-1 * tup[1], tup[0], tup[2])
    elif orient_div == 3:
        inter_tup = (tup[1], tup[2], tup[0])
    elif orient_div == 4:
        inter_tup = (tup[2], tup[0], tup[1])
    else: #orient_div == 5
        inter_tup = (-1 * tup[2], tup[1], tup[0])
    
    if root_div == 0:
        final_tup = (inter_tup[0], inter_tup[1], inter_tup[2])
    elif root_div == 1:
        final_tup = (-1 * inter_tup[0], -1 * inter_tup[1], inter_tup[2])
    elif root_div == 2:
        final_tup = (-1 * inter_tup[0], inter_tup[1], -1 * inter_tup[2])
    else: #root_div == 3
        final_tup = (inter_tup[0], -1 *inter_tup[1], -1 * inter_tup[2])
    return final_tup

def get_vector(a, b):
    return tuple(map(lambda i, j: i - j, b, a))

def add_tuples(p1, p2):
    return tuple(map(lambda i, j: i + j, p1, p2))

def in_range(tup):
    return -1000 < tup[0] < 1000 and -1000 < tup[1] < 1000 and -1000 < tup[2] < 1000

def attempt_combine(s1, s2, o):

    #print("attempt combine:")

    for p1 in s1:
        for p2 in s2:

            vector = get_vector(get_oriented_tuple(p2, o), p1)
            correct_count = 0
            #print(f"p1: {p1} p2: {p2} oriented: {get_oriented_tuple(p2, o)} vector: {vector}")
            if get_oriented_tuple(p2, o) == (-686, 422, -578) and p1 == (-618,-824,-621):
                print(f"{get_oriented_tuple(p2, o)}")
                print(vector)


            for p_test in s2:
                test_point = add_tuples(get_oriented_tuple(p_test, o), vector)
                if in_range(test_point):
                    if test_point in s1:
                        correct_count += 1
                    else:
                        break
                if correct_count >= 12:
                    return vector
    
    return False

def find_combined(scanners):
    overlaps = []
    mapped = set([0])
    while len(mapped) < len(scanners):
        for scanner_idx in range(len(scanners)):
            if scanner_idx in mapped:
                for scanner_idx_2 in range(len(scanners)):
                    if scanner_idx_2 not in mapped:
                        for orientation in range(24):
                            v = attempt_combine(scanners[scanner_idx], scanners[scanner_idx_2], orientation)
                            if v:
                                print("OVERLAP FOUND: ")
                                print(scanner_idx)
                                print(scanner_idx_2)
                                mapped.add(scanner_idx_2)
                                overlaps.append((scanner_idx, scanner_idx_2, v, orientation))
    return overlaps

def get_manhatten_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def main():

    with open("./input.txt") as f:
        input_lines = [line.strip() for line in f.readlines()]

    scanners = []

    for line in input_lines:
        if "scanner" in line:
            scanners.append(set())
        elif "," in line:
            scanners[-1].add(tuple(map(int, line.split(","))))
    
    scanner_locations = [set([(0, 0, 0)]) for i in scanners]
    print(scanner_locations)
    
    overlaps = find_combined(scanners)
    overlaps.reverse()

    #print(overlaps)

    for to_set, from_set, vector, orientation in overlaps:
        for point in scanners[from_set]:
            new_point = add_tuples(get_oriented_tuple(point, orientation), vector)
            scanners[to_set].add(new_point)
        for scanner_loc in scanner_locations[from_set]:
            new_point = add_tuples(get_oriented_tuple(scanner_loc, orientation), vector)
            scanner_locations[to_set].add(new_point)
        #print(f"{from_set} -> {to_set}")
        #print(len(scanners[to_set]))

    print(f"Part A: {len(scanners[0])}")
    #print(scanner_locations[0])
    
    manhatten = 0
    for a in scanner_locations[0]:
        for b in scanner_locations[0]:
            manhatten = max(get_manhatten_distance(a, b), manhatten)
    
    print(f"Part B: {manhatten}")

if __name__ == "__main__":
    main()