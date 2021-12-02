from read_inputs import readFromFile
fileName = "d2_inputs.txt"
fileName = "real_inputs2.txt"
 
class Submarine:
    def __init__(self):
        self._depth = 0
        self._horizontal_position = 0

    def change_depth(self, delta):         # called by "down/up X"
        self._depth += delta

    def change_position(self, delta):      # called by "forward X"
        self._horizontal_position += delta

    def get_final(self):
        return self._depth * self._horizontal_position

class Submarine2:
    def __init__(self):
        self._aim = 0
        self._depth = 0
        self._horizontal_position = 0

    def change_aim(self, delta):
        self._aim += delta

    def handle_forward(self, delta):
        self._horizontal_position += delta
        self._depth += self._aim * delta

    def get_final(self):
        return self._depth * self._horizontal_position

def part1(directions, sub):
    for x in directions:
        order, value = x.split()
        value = int(value)              #string to int

        if order.startswith("f"):       #forward X
            sub.change_position(value)
        elif x.startswith("u"):         #upwards X
            sub.change_depth(value * -1)
        else:                           #down X
            sub.change_depth(value)

    print("PART 1:", sub.get_final())

def part2(directions, sub):
    for x in directions:
        order, value = x.split()
        value = int(value)              # string to int

        if order.startswith("d"):       # down X
            sub.change_aim(value)
        elif order.startswith("u"):     # upwards X
            sub.change_aim(value * -1)
        else:                           # forward X
            sub.handle_forward(value)

    print("PART 2:", sub.get_final())

def main():
    directions = readFromFile(fileName)
    # print(directions)

    sub = Submarine()
    part1(directions, sub)

    sub2 = Submarine2()
    part2(directions, sub2)

main()
