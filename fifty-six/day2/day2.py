import operator
from itertools import accumulate

inp = [
    (x[0], int(y))
    for x, y in map(str.split, map(str.strip, open("../input/day2.txt").readlines()))
]
xs, ys = (
    [y if x == "f" else 0 for x, y in inp],
    [{"u": -1, "d": 1}.get(x, 0) * y for x, y in inp],
)
print(sum(xs) * sum(ys))
print(sum(xs) * sum(map(operator.mul, xs, accumulate(ys))))
