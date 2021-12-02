dir = "pest/day1/inputs/"
fileName = "inputs.txt"
fileName = "real_inputs.txt"

def readFromFile(name):
    with open(name, "r") as file:
        data = file.readlines()
        data = [int(x.strip()) for x in data]
        print(data)
        return data

def main():
    total = 0
    numbers = readFromFile(dir + fileName)

    a = numbers[0] + numbers[1] + numbers[2]

    for x, y, z in zip(numbers[1:], numbers[2:], numbers[3:]):
        b = x + y + z
        total += 1 if b > a else 0
        a = b

    print(total)

main()
