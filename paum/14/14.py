from collections import Counter

with open("./input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

polymer = list(arr[0])
insertions = []
rules = dict()
table = dict()
steps = 40

#def count

for rule in arr:
    if "->" in rule:
        rs = [part.strip() for part in rule.split("->")]
        rules[rs[0]] = [rs[0][0] + rs[1] , rs[1] +  rs[0][1], rs[1]]

for combo in rules.keys():
    table[combo] = [None] * (steps + 1)

def count_elements(combo, step):

    print("Recurse: " + combo + " " + str(step))

    if combo not in table.keys():
        return Counter()

    if (table[combo][step]):
        return table[combo][step]

    if (step == 0):
        table[combo][step] = Counter(combo)

    else:
        r = rules[combo]
        result = count_elements(r[0], step - 1) + count_elements(r[1], step - 1) - Counter(r[2])
        table[combo][step] = result
    
    return table[combo][step]

#print(rules)
#print(table)

c = Counter()
for i in range(len(polymer) - 1):
    c += count_elements(polymer[i] + polymer[i + 1], steps)
    #print(c)

c -= Counter(polymer[1:-1])

print(c)
print(c.most_common())
print(c.most_common()[0][1] - c.most_common()[-1][1])



