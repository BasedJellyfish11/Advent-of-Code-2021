from itertools import product
from fractions import Fraction
import numpy as np

with open("../input/day5.txt") as f:
    f_lines = [x.strip() for x in f.readlines()]

lines = set()
for line in f_lines:
    l, r = line.split("->")

    l = tuple(int(x) for x in l.strip().split(","))
    r = tuple(int(x) for x in r.strip().split(","))

    lines.add((l, r))

def slope(start, end):
    (x0, y0) = start
    (x1, y1) = end

    return ((x1 - x0), (y1 - y0))

grid = np.zeros((1000, 1000))

vh = set((s, e) for s, e in lines if 0 in slope(s, e))

for l in vh:
    (x0, y0), (x1, y1) = l
    (a, b) = sorted((x0, x1))
    (c, d) = sorted((y0, y1))
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            grid[x, y] += 1

print(np.sum(grid >= 2))

for diag in lines - vh:
    dx, dy = slope(*diag)

    f = Fraction(dy, dx)
    dy = f.numerator
    dx = f.denominator

    if dx < 0:
        dx *= -1
        dy *= -1

    s, e = diag

    x, y = min((s, e), key=lambda h: h[0])
    x_end, y_end  = e if s == (x, y) else s

    while x != x_end:
        grid[x][y] += 1
        x += dx
        y += dy

    assert y == y_end

    grid[x][y] += 1

print(np.sum(grid >= 2))
