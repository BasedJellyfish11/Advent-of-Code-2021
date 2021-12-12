from math import copysign, isnan
import numpy as np

test = False

with open(f"../input/{'test_' if test else ''}day7.txt") as f:
    # :pinchers:
    crabs = np.array([int(x) for x in f.read().strip().split(",")])

def sim_p1(h):
    # d/dh | x - h | = sgn(h - x)
    return np.sum(np.abs(crabs - h)), np.sum(np.sign(h - crabs))

def sim_p2(h):
    # let k = |x_i - h|
    # cost = k * (k + 1) / 2
    # so d/dh = sgn(h - x) / 2 + (h - x)

    d   = np.abs(crabs - h)
    err = np.sum((d * (d + 1)) / 2)
    dh  = np.sum(.5 * np.sign(h - crabs) + (h - crabs))

    return err, dh

def solve(sim):
    # very random
    sol = 5
    alpha = .00005

    for i in range(100000):
        err, dh = sim(sol)

        if abs(dh) < 1e-4:
            break

        sol -= dh * alpha

    err, _ = sim(round(sol))
    print(f"sol: {sol} -> {round(sol)}, err: {err}")

if __name__ == "__main__":
    solve(sim_p1)
    solve(sim_p2)
