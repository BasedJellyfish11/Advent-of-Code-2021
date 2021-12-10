import statistics

with open("./input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

corrosponding = {'[': ']', '{': '}', '<': '>', '(': ')'}
score = {']': 57, '}': 1197, '>': 25137, ')': 3}
score2 = {'[': 2, '{': 3, '<': 4, '(': 1}

total_score = 0
total_score2 = []

for seq in arr:
    stack = []
    valid = True
    for char in seq:
        if char in corrosponding.keys():
            stack.append(char)
        else:
            end_char = stack.pop()
            if char != corrosponding[end_char]:
                total_score += score[char]
                valid = False
                break
    if (valid):
        string_score = 0
        for i in range(len(stack)):
            string_score *= 5
            string_score += score2[stack.pop()]
        total_score2.append(string_score)

print(total_score)
print(statistics.median(total_score2))