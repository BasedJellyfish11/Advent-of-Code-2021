from collections import defaultdict
from sys import argv
from skimage.util.shape import view_as_windows as windows
import numpy as np

test = len(argv) == 2 and bool(argv[1]) 

def parse():
    print(f"test: {test}")
    with open("../input/" + ('test_' if test else '') + "day20.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    
    alg = lines[0]
    
    img = np.array([[1 if x == '#' else 0 for x in l] for l in lines[2:]])

    return alg, img

def bin_num(num):
    return sum(2**(len(num) - i - 1) * x for i, x in enumerate(num))

def f(alg, w):
    return 1 if alg[bin_num(w.reshape(1, -1)[0])] == '#' else 0

def apply(alg, img, a=False):
    img = np.pad(img, [5, 5], constant_values=(1,) if a else (0,))

    out = ""
    for r in windows(img, (3, 3)):
        for w in r:
            n = bin_num(w.reshape(1, -1)[0])
            out += alg[n]
        out += "\n"

    return np.array([[1 if x == '#' else 0 for x in l] for l in out.split()])

def solve(alg, img):
    for _ in range(25):
        img = apply(alg, img)
        img = apply(alg, img, True)

    print(np.sum(img == 1))

if __name__ == "__main__":
    solve(*parse())
