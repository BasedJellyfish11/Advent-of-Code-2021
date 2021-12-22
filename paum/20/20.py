import numpy as np

def pad_image(a, p):
    return np.pad(a, ((1, 1), (1, 1)), 'constant', constant_values=((p,p), (p,p)))

def solve(bin_list):
    tot = 0
    power = 1
    for num in np.flip(bin_list):
        if num == '#':
            tot += power
        power = power * 2
    return tot

def solve_pixel(image, i, j):
    local_pixels = image[i:i+3, j:j+3]
    bin_coded = local_pixels.flatten()
    return solve(bin_coded)

def main():

    with open("./input.txt") as f:
        input_file = [line.strip() for line in f.readlines()]

    decoder = input_file[0]

    image = np.array(input_file[2:])
    image = [np.array(list(line)) for line in image]

    padding = '.'

    image = pad_image(image, padding)
    for mode in range(50):
        new_image = np.array(image)
        #print(new_image)
        image = pad_image(image, padding)
        for i, outer in enumerate(new_image):
            for j, inner in enumerate(outer):
                new_image[i, j] = decoder[solve_pixel(image, i, j)]
        
        padding = decoder[0] if padding == '.' else decoder[-1]

        image = pad_image(new_image, padding)

        if mode == 1:
            print(f"Part 1: {np.count_nonzero(image=='#')}")

    print(f"Part 2: {np.count_nonzero(image=='#')}")

if __name__ == "__main__":
    main()