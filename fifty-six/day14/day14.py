from collections import Counter, defaultdict

def parse():
    test = False
    
    with open(f"../input/{'test_' if test else ''}day14.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    
    polymer = lines[0]
    rules = {}
    
    for line in lines[2:]:
        a, b = line.split("->")
        rules[a.strip()] = b.strip()

    return polymer, rules

def recur(poly, rules, n):
    if n == 0: 
        return poly

    new_dict = defaultdict(int)

    for pair, v in poly.items():
        new = rules[pair]
        new_dict[pair[0] + new] += v
        new_dict[new + pair[1]] += v

    return recur(new_dict, rules, n - 1)

def count(poly):
    letters = defaultdict(int)
    for ind, (key, v) in enumerate(poly.items()):
        for l in key[1 if ind == 0 else 0:]:
            letters[l] += v

    c = Counter(letters)

    return (max(c.values()) // 2 - min(c.values()) // 2 - 1)


def dict_from_str(poly):
    poly_dict = defaultdict(int)
    
    for window in zip(poly, poly[1:]):
        poly_dict[''.join(window)] += 1

    return poly_dict

def solve(polymer, rules):
    poly_dict = dict_from_str(polymer)
    p1 = count(recur(poly_dict, rules, 10))
    p2 = count(recur(poly_dict, rules, 40))

if __name__ == "__main__":
    solve(*parse())
