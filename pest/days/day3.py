import numpy as np

from read_inputs import read_file
fileName = "d3_inputs.txt"
# fileName = "real_inputs3.txt"

def decode_binary_string(bin_string):
    incoming = bin_string[0]
    length = len(incoming)
    total = y = 0
    for x in incoming:
        total += 2 ** (length - 1 - y) if int(x) > 0.5 else 0 #cringe
        y += 1
    print("decode_binary_string:", total)
    return total

def main():
    total = 0
    numbers = np.asarray(read_file(fileName))        # returns list of contents of file as strings

    print(numbers)

    message_length = len(numbers[0])
    c = 0

    c_2 = np.zeros(message_length)

    for z in range(message_length):
        y = [x[z] for x in numbers]
        y = sum(list(map(int, y))) / len(y)

        c += 2 ** (message_length-1-z) if y > 0.5 else 0 #cringe

    d = c ^ ((2 ** message_length) - 1) #xor with (2^x - 1) to flip bits

    print("PART 1:", c*d)

    print("\n\nPART 2 BEGINNING \n\n")

    numbers = np.sort(numbers)
    co2_nums = numbers

    for a in range(message_length):
        col = [x[a:(a+1)] for x in numbers]
        col = np.asarray(col).astype(int)
        median = 1 if np.median(col) else 0

        remove_index = np.where(col!=median)
        numbers = np.delete(numbers, remove_index)
    print("Oxygen Generator Number:", numbers)

    for a in range(message_length):
        if len(co2_nums) == 1: break
        col = [x[a:a+1] for x in co2_nums]
        col = np.asarray(col).astype(int)
        median = 1 if np.median(col) else 0
        remove_index = np.where(col==median)
        co2_nums = np.delete(co2_nums,remove_index)

    print("CO2 Scrubber Rating:", co2_nums)
    c = decode_binary_string(numbers)
    d = decode_binary_string(co2_nums)
    print("O2*CO2:", c * d)

main()
