import operator
from functools import partial, reduce

test = False
with open(f"../input/{'test_' if test else ''}day16.txt") as f:
    s = ''.join(f'{int(x, 16):04b}' for x in f.read().strip())

def parse_literal(ind):
    start = ind

    while s[ind] == "1":
        ind += 5
    
    ind += 5

    literal = list(s[start : ind])
    del literal[::5]

    return ind, int(''.join(literal), 2)

def parse_packet(ind):
    V = int(s[ind: ind + 3], 2)
    T = int(s[ind + 3: ind + 6], 2)

    ind += 6

    # Literal
    if T == 4:
        return (*parse_literal(ind), V)

    def apply(f, seq):
        return f(seq[0], seq[1])

    # Operator
    func = {
            0: sum,
            1: partial(reduce, operator.mul),
            2: min,
            3: max,
            5: partial(apply, operator.gt),
            6: partial(apply, operator.lt),
            7: partial(apply, operator.eq),
    }[T]

    ver_sum = V
    values = []

    if s[ind] == "0":
        # next 15 bits are total length in bits of subpackets
        bits = int(s[ind + 1: ind + 16], 2)
        ind += 16

        start = ind

        values = []
        while (ind - start) < bits:
            ind, val, dv = parse_packet(ind)

            ver_sum += dv
            values.append(val)
    else:
        # next 11 bits are # of sub-packets contained by this packet
        packets = int(s[ind + 1: ind + 12], 2)
        ind += 12

        for _ in range(packets):
            ind, val, dv = parse_packet(ind)

            ver_sum += dv
            values.append(val)

    return ind, func(values), ver_sum

print(parse_packet(0))
