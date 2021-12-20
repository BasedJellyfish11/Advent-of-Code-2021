import numpy as np


fmt_dict = {
    'sep': '\n\n'
    }

def step(image, key):
    image[:] = key[
          1 * np.roll(np.roll(image, -1, axis=0), -1, axis=1) +
          2 * np.roll(image, -1, axis=0) +
          4 * np.roll(np.roll(image, -1, axis=0),  1, axis=1) +
          8 * np.roll(image, -1, axis=1) +
         16 * image +
         32 * np.roll(image,  1, axis=1) +
         64 * np.roll(np.roll(image,  1, axis=0), -1, axis=1) +
        128 * np.roll(image,  1, axis=0) +
        256 * np.roll(np.roll(image,  1, axis=0),  1, axis=1)
        ]

def solve(data, N=50):
    key = np.array(list(data[0]))
    key = np.where(key == '#', 1, 0)
    
    image = np.array([list(line) for line in data[1].split('\n')])
    image = np.pad(np.where(image == '#', 1, 0), N)
    
    for iteration in range(1, N+1):
        step(image, key)
        if iteration == 2:
            ans_a = np.count_nonzero(image)

    return ans_a, np.count_nonzero(image)