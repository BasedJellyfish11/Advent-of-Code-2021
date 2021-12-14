from itertools import permutations

test = False

with open(f"../input/{'test_' if test else ''}day8.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    signals = []

    for line in lines:
        a, b = line.split("|")
        a, b = a.strip(), b.strip()
        signals.append((a.split(" "), b.split(" ")))

segments = {
        0: {'a', 'b', 'c', 'e', 'f', 'g'},
        1: {'c', 'f'},
        2: {'a', 'c', 'd', 'e', 'g'},
        3: {'a', 'c', 'd', 'f', 'g'},
        4: {'b', 'c', 'd', 'f'},
        5: {'a', 'b', 'd', 'f', 'g'},
        6: {'a', 'b', 'd', 'e', 'f', 'g'},
        7: {'a', 'c', 'f'},
        8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        9: {'a', 'b', 'c', 'd', 'f', 'g'},
}

segments = { tuple(sorted(y)) : x for x, y in segments.items() }

def p1():
    return sum(sum(1 for x in out if len(x) in [2, 4, 3, 7]) for _, out in signals)

def map_from(letters, value):
    return tuple(sorted(letters[x] for x in value))

def satisfied(inps, letters):
    return { segments.get(map_from(letters, x)) for x in inps } == set(range(0, 10))

def resolve(signal):
    letters_li = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]

    inps, outs = signal

    for permutation in permutations(letters_li, 7):
        letters = {}

        for ind, l in enumerate(list(letters_li)):
            letters[l] = permutation[ind]

        if satisfied(inps, letters):
            break

    return sum(10**(3 - ind) * segments[map_from(letters, out)] for ind, out in enumerate(outs))


def p2():
    return sum(resolve(s) for s in signals)

if test:
    assert p1() == 26
    assert p2() == 61229
else:
    print(p1())
    print(p2())
