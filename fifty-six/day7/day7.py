from math import copysign, isnan

test = False

with open(f"../input/{'test_' if test else ''}day7.txt") as f:
    # :pinchers:
    crabs = [int(x) for x in f.read().strip().split(",")]

def sim_p1(h):
    # d/dh | x - h | = sgn(h - x)
    err = 0
    dh = 0
    
    for crab in crabs:
        err += abs(crab - h)
        dh += copysign(1, h - crab)
    
    return err, dh

def sim_p2(h):
    # let k = |x_i - h|
    # cost = k * (k + 1) / 2
    # so d/dh = sgn(h - x) / 2 + (h - x)

    err = 0
    dh = 0

    for crab in crabs:
        if crab == h:
            continue

        diff = abs(crab - h)
        err += (diff * (diff + 1)) / 2
        dh += .5 * copysign(1, h - crab) + (h - crab)

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
