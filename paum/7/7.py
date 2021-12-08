import statistics

with open("./input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

x_positions = list(map(lambda x: int(x), arr[0].split(",")))

middle = statistics.median(x_positions)

# PART A

tot = sum(map(lambda x: abs(middle - x), x_positions))
print(tot)

#PART B

fuel_costs = [0] * (max(x_positions) + 1)
cost = 0

for i in range(len(fuel_costs)):
    cost += i
    fuel_costs[i] = cost

total_fuel = []

for fuel_position in range(max(x_positions)):
    tot = 0
    for x in x_positions:
        tot += fuel_costs[abs(x - fuel_position)]
    total_fuel.append(tot)

print(min(total_fuel))
