from read_inputs import read_file
fileName = "d1_inputs.txt"
fileName = "real_inputs1.txt"

def main():
    total = 0
    numbers = read_file(fileName)        # returns list of contents of file as strings
    numbers = list(map(int, numbers))       # cast all to ints from strings

    for a,b in zip(numbers, numbers[1:]):   # compare subsequent indices
        total += 1 if b > a else 0 # if bigger than previous, add
    print("part1: ", total)

    total = 0

    a = numbers[0] + numbers[1] + numbers[2]
    for x, y, z in zip(numbers[1:], numbers[2:], numbers[3:]):
        b = x + y + z
        total += 1 if b > a else 0
        a = b
    print("part2: ", total)

main()
