import copy

class snail_number:

    def __init__(self, parent, is_number, value):
        self.parent = parent
        self.is_number = is_number
        self.value = value
    
    def magnitude(self):
        if self.is_number:
            return self.value
        else:
            return 3 * self.left_child.magnitude() + 2 * self.right_child.magnitude()
    
    def print_self(self):
        print(self.describe_self())

    def describe_self(self):
        if self.is_number:
            return self.value
        else:
            return f"[{self.left_child.describe_self()},{self.right_child.describe_self()}]"

    def children(self):
        return (self.left_child, self.right_child)

    left_child = None
    right_child = None

def find_comma(snail_string):

    nested = 0
    
    for i, char in enumerate(snail_string):
        if char == "," and nested == 1:
            return i
        elif char == "[":
            nested += 1
        elif char == "]":
            nested -= 1

def add_snail_numbers(sn1, sn2):
    snail_sum = snail_number(None, False, None)
    snail_sum.left_child = sn1
    sn1.parent = snail_sum
    snail_sum.right_child = sn2
    sn2.parent = snail_sum

    return snail_sum

def parse_input_string(string, p):

    #print(f"Parsing: {string}")

    if string.isdigit():
        return snail_number(p, True, int(string))
    
    x = snail_number(p, False, None)
    comma_location = find_comma(string)
    x.left_child = parse_input_string(string[1:comma_location], x)
    x.right_child = parse_input_string(string[comma_location + 1: -1], x)
    return x

def find_explode(sn, depth):
    if sn.is_number:
        return None
    elif depth >= 4:
        return sn

    for child in sn.children():
        fe = find_explode(child, depth + 1)
        if fe:
            return fe

    return None

def increment_left(sn, val):

    sn_parent = sn.parent

    while sn_parent and sn_parent.left_child == sn:
        sn = sn_parent
        sn_parent = sn.parent

    if not sn_parent:
        return
    
    sn = sn_parent.left_child

    while not sn.is_number:
        sn = sn.right_child
    
    sn.value += val

def increment_right(sn, val):

    sn_parent = sn.parent

    while sn_parent and sn_parent.right_child == sn:
        sn = sn_parent
        sn_parent = sn.parent

    if not sn_parent:
        return
    
    sn = sn_parent.right_child

    while not sn.is_number:
        sn = sn.left_child
    
    sn.value += val

def snail_explode(sn):
    increment_left(sn, sn.left_child.value)
    increment_right(sn, sn.right_child.value)
    sn.is_number = True
    sn.value = 0

def find_split(sn):
    if sn.is_number:
        return sn if sn.value >= 10 else None

    for child in sn.children():
        fs = find_split(child)
        if (fs):
            return fs

    return None

def snail_split(sn):
    sn.is_number = False
    sn.left_child = snail_number(sn, True, sn.value // 2)
    sn.right_child = snail_number(sn, True, (sn.value + 1) // 2 )

def snail_reduce(sn):

    while (True):

        #sn.print_self()

        num_to_explode = find_explode(sn, 0)
        num_to_split = find_split(sn)

        if num_to_explode:
            snail_explode(num_to_explode)
            
        elif num_to_split:
            snail_split(num_to_split)
        
        else:
            return sn

def part_1(numbers):

    running_sum = numbers[0]

    for num in numbers[1:]:
        running_sum = add_snail_numbers(running_sum, num)
        snail_reduce(running_sum)

    running_sum.print_self()
    print(running_sum.magnitude())

def part_2(numbers):

    sn_max = 0

    for sn1 in numbers:
        for sn2 in numbers:
            if sn1 != sn2:
                sn1_copy = copy.deepcopy(sn1)
                sn2_copy = copy.deepcopy(sn2)
                sn_max = max(sn_max, snail_reduce(add_snail_numbers(sn1_copy, sn2_copy)).magnitude())
                #print(sn_max)

    print(sn_max)

def main():

    with open("input.txt") as f:
        numbers = [line.strip() for line in f.readlines()]

    numbers = [parse_input_string(n, None) for n in numbers]
    numbers_2 = copy.deepcopy(numbers)

    part_1(numbers)
    part_2(numbers_2)

main()