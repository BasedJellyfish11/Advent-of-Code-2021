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

    for a,b in zip(numbers, numbers[1:]):

        total += 1 if b > a else 0

    print(total)

main()
