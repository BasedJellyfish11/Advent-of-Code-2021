from collections import Counter

with open("../input/day3.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

gamma = ""
epsilon = ""

for a in zip(*data):
    common = sorted(Counter(a).items(), key=lambda x: x[1])
    gamma   += common[0][0]
    epsilon += '0' if common[0][0] == '1' else '1'

print(gamma, epsilon)
gamma, epsilon = int(gamma, 2), int(epsilon, 2)
print(gamma, epsilon)

print(gamma * epsilon)

possibles = data.copy()
n = 0

while len(possibles) != 1:
    c = Counter(x[n] for x in possibles)
    item, count = sorted(Counter(x[n] for x in possibles).items(), key=lambda a: (a[1], a[0] == "1"))[0]
    possibles = [x for x in possibles if x[n] == item]

    n += 1

oxygen = possibles[0]

possibles = data.copy()
n = 0
while len(possibles) != 1:
    c = Counter(x[n] for x in possibles)
    item, count = sorted(Counter(x[n] for x in possibles).items(), key=lambda a: (a[1], a[0] != "0"))[-1]
    possibles = [x for x in possibles if x[n] == item]

    n += 1

co2 = possibles[0]

print(oxygen, co2)
oxygen, co2 = int(oxygen, 2), int(co2, 2)
print(oxygen * co2)
