from pprint import pprint

release = True

file = "test_day11" if not release else "day11.txt"

with open(f"../input/{file}") as f:
    lines = [x.strip() for x in f.readlines()]

lines = [[int(x) for x in line] for line in lines]

def sim_step():
    octo_flashes = set()

    max_h, max_k = len(lines), len(lines[0])

    def valid(h, k):
        return (0 <= h < max_h) and (0 <= k < max_k)


    def flash(h, k):
        if (h, k) in octo_flashes:
            return

        octo_flashes.add((h, k))

        for h_a in range(-1, 2):
            for k_a in range(-1, 2):
                if (h_a, k_a) == (0, 0):
                    continue

                if not valid(h + h_a, k + k_a):
                    continue

                # inc adj by one
                lines[h + h_a][k + k_a] += 1

                if lines[h + h_a][k + k_a] > 9:
                    flash(h + h_a, k + k_a)

    for i, r in enumerate(lines):
        for j, o in enumerate(r):
            lines[i][j] += 1

    for i, row in enumerate(lines):
        for j, octo in enumerate(row):
            if octo > 9:
                flash(i, j)

    for (i, j) in octo_flashes:
        lines[i][j] = 0

    return len(octo_flashes), len(octo_flashes) == max_h * max_k

pprint(lines)

flashes = 0
all_flash = None
for step in range(100):
    (inc_flashes, all_flashed) = sim_step()
    flashes += inc_flashes

    if all_flashed:
        all_flash = step + 1
print(flashes)

while not all_flash:
    step += 1
    (_, all_flashed) = sim_step()

    if all_flashed:
        all_flash = step + 1

print(all_flash)
