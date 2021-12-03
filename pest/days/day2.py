from read_inputs import read_file
fileName = "d2_inputs.txt"
fileName = "real_inputs2.txt"

class Sub:
    def __init__(self, type):
        self._depth = self._aim = self._horizontal_position = 0
        self._type = type

    def change_depth(self, delta):
        if self._type: self._aim += delta
        else: self._depth += delta

    def change_position(self, delta):
        if self._type: self._depth += delta * self._aim
        self._horizontal_position += delta

    def get_final(self): return self._horizontal_position * self._depth

def part1(directions, sub):
    for x in directions:
        # credit to verulean for showing me this and 56 for explaining it
        order, value = (lambda i,j: (i, int(j)))(*x.split())

        if order.startswith("f"):   sub.change_position(value)
        elif x.startswith("u"):     sub.change_depth(value * -1)
        else:                       sub.change_depth(value)

def main():
    directions = read_file(fileName)

    for x in range(2):
        e = Sub(x)
        part1(directions, e)
        print("PART", x+1, ":", e.get_final())

main()
