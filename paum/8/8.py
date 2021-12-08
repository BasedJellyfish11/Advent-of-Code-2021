with open("./input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

for i in range(len(arr)):
    line = arr[i]
    #print(line)
    line = line.split("|")
    #print(line)
    line = [part.strip().split(" ") for part in line]
    #print(line)
    arr[i] = line

digit_count = 0
uniques = [2, 4, 3, 7]

#print(arr[0])
for line in arr:
    output = line[1]
    for sequence in output:
        if len(sequence) in uniques:
            digit_count += 1

print(digit_count)

# PART B


number = {677376: 8, 21168: 5, 12544: 2, 28224: 3, 576: 7, 169344: 9, 84672: 6, 3024: 4, 96768: 0, 72: 1}

sum_total = 0

for testline in arr:

    d = dict.fromkeys(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 0)

    inputs = testline[0]
    outputs = testline[1]

    number_total = ''

    for num in inputs:
        for char in num:
            d[char] += 1

    for num in outputs:
        mult = 1
        for char in num:
            mult *= d[char]
        number_total += str(number[mult])

    print(number_total)
    sum_total += int(number_total)

print(sum_total)
