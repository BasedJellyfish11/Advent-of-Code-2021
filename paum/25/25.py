import numpy as np

def main():

    with open("./input.txt") as f:
        floor = np.array([list(line.strip()) for line in f.readlines()])

    max_y, max_x = floor.shape
    #print(f"{floor}\n")

    for i in range(1, 600):
        moved = False

        floor_state = np.array(floor)
        for y, x in np.ndindex(floor_state.shape):
            lad = floor_state[y, x]
            if lad == ">" and floor_state[y, (x + 1) % max_x] == ".":
                floor[y, x] = "."
                floor[y, (x + 1) % max_x] = ">"
                moved = True

        floor_state = np.array(floor)
        for y, x in np.ndindex(floor_state.shape):
            lad = floor_state[y, x]
            if lad == "v" and floor_state[(y + 1) % max_y, x] == ".":
                floor[y, x] = "."
                floor[(y + 1) % max_y, x] = "v"
                moved = True

        #print(f"{floor}\n")
        #print(i, flush=True)

        if not moved:
            print(i)
            quit()

if __name__ == "__main__":
    main()