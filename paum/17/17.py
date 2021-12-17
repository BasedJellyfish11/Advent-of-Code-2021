with open("./input.txt") as f:
    arr = [ line.strip() for line in f.readlines()]

annoying = arr[0].replace("=", "|").replace(".", "|").replace(",", "|").replace(" ", "|").split("|")

nums = [int(thing) for thing in annoying if thing.replace("-", "").isnumeric()]

def contained(loc):
    return nums[0] <= loc[0] <= nums[1] and nums[2] <= loc[1] <= nums[3]

def increment(paws, vel):
    paws[0] += vel[0]
    paws[1] += vel[1]
    if (vel[0] > 0):
        vel[0] -= 1
    elif vel[0] < 0:
        vel[0] += 1
    vel[1] -= 1

all_vels = set()

max_max_y = 0

for x in range(0, nums[1] + 5):
    for y in range(nums[2] - 5, 100):
        paws = [0, 0]
        vel = [x, y]
        max_y = 0
        while(paws[1] > nums[2]):
            increment(paws, vel)
            max_y = max(max_y, paws[1])
            if contained(paws):
                max_max_y = max(max_y, max_max_y)
                if (x, y) not in all_vels:
                    all_vels.add((x, y))
                print(x, y, max_y)

print(len(all_vels))
print(max_max_y)






