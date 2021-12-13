from read_inputs import read_file
fileName = "d10_inputs.txt"
fileName = "real_inputs10.txt"

import numpy as np

openers = np.asarray(["{", "(", "<", "["])
closers = np.asarray(["}", ")", ">", "]"])

def get_index(x):
    # x = some char (either opener or closer tag)
    # [0] because where returns all occurences, only need first
    return np.where(closers == x)[0]

def get_opposite_char(inc_char):
    if np.any(np.isin(inc_char, openers)):
        return closers[np.where(openers == inc_char)[0]]
    else:
        return openers[np.where(closers == inc_char)[0]]

def print_score(illegal_chars):
    total = 0
    for x in illegal_chars:
        if x == ")": total += 3
        elif x == "]": total += 57
        elif x == "}": total += 1197
        else: total += 25137
    return total

def get_p2_scores(char_to_score):
    if char_to_score == ")": return 1
    elif char_to_score == "]": return 2
    elif char_to_score == "}": return 3
    else: return 4

def main():
    total = 0
    numbers = np.asarray(read_file(fileName))   # returns list of contents of file as strings

    illegal_chars = np.asarray([])
    rows_to_remove = np.asarray([], dtype=np.uint32)
    p2_array = np.asarray([[]])

    for ind_to_remove, y in enumerate(numbers):
        seen_openers = np.asarray([])
        dont_use = False
        for index, x in enumerate(y):
            if np.any(np.isin(x, openers)):
                seen_openers = np.append(seen_openers, x)
            else: # seen closing tag
                # print("seen closing tag: comparing --", seen_openers[-1], x)
                e = get_opposite_char(x)
                if e != seen_openers[-1]:
                    print(f"illegal character found at index {index}: {x} -- in string {y}\n")
                    illegal_chars = np.append(illegal_chars, x)
                    rows_to_remove = np.append(rows_to_remove, ind_to_remove)
                    dont_use = True
                    break
                seen_openers = np.delete(seen_openers, -1, 0)
        if not dont_use:
            print(np.array2string(seen_openers))
            temp = ""
            # temp += [x for x in seen_openers]
            for x in seen_openers:
                temp += x
            p2_array = np.append(p2_array, [temp])
        print(f"run {ind_to_remove} -- p2_array:", p2_array)

    print("illegal chars seen: ", illegal_chars)
    print(f"score: {print_score(illegal_chars)}")

    e = np.asarray([], dtype=np.uint64)
    for y in p2_array:
        print(y)
        total = 0
        for x in reversed(y):
            print(get_opposite_char(x), end="")
            total = 5 * total + get_p2_scores(get_opposite_char(x))
            print(total)
        e = np.append(e, total)
    print("part 2: ", np.sort(e)[(e.shape[0]-1) // 2])


main()
