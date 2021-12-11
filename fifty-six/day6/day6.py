import numpy as np

fish = np.genfromtxt("../input/day6.txt", delimiter=",")
fish = np.array([np.sum(fish == n) for n in range(0, 9)])

for n in [80, 256 - 80]:
    for _ in range(n):
        fish = np.roll(fish, -1)
        fish[6] += fish[8]

    print(np.sum(fish))
