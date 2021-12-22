import numpy as np
import time

class area:
    
    def __init__(self, x_coords, y_coords, z_coords, parity):
        self.x_coords = x_coords
        self.y_coords = y_coords
        self.z_coords = z_coords
        self.overlaps = []
        self.parity = parity

    def overlapping(self, a, b):
        return a[1] > b[0] and b[1] > a[0]
    
    def add_overlap(self, new_area):
        if self.overlapping(self.x_coords, new_area.x_coords) and self.overlapping(self.y_coords, new_area.y_coords) and self.overlapping(self.z_coords, new_area.z_coords):
            x = (max(self.x_coords[0], new_area.x_coords[0]), min(self.x_coords[1], new_area.x_coords[1]))
            y = (max(self.y_coords[0], new_area.y_coords[0]), min(self.y_coords[1], new_area.y_coords[1]))
            z = (max(self.z_coords[0], new_area.z_coords[0]), min(self.z_coords[1], new_area.z_coords[1]))
            self.overlaps.append(area(x, y, z, 1))
    
    def get_parity(self):
        return self.parity

    def dist(self, i):
        return i[1] - i[0]

    def get_box_area(self):
        return self.dist(self.x_coords) * self.dist(self.y_coords) * self.dist(self.z_coords)

    def __str__(self):
        my_str = f"x: {self.x_coords} y: {self.y_coords} z: {self.z_coords}"
        for a in self.overlaps:
            my_str += f"\n\t{a}"
        return my_str

def get_instructions():

    with open("./input.txt") as f:
        instructions = [line.strip() for line in f.readlines()]

    for i, line in enumerate(instructions):
        onoff, input_string = line.split(' ')
        onoff = 0 if onoff == 'off' else 1
        arr = [int(num) for num in input_string.replace('x=', '').replace('y=', '').replace('z=', '').replace('..',',').split(',')]
        instructions[i] = (onoff, arr)

    return instructions

def dist(x):
    return x[1] - x[0]
    
def get_total_area(area_list):

    #print("Getting Total Area of List")

    if len(area_list) == 0:
        return 0
    
    elif len(area_list) == 1:
        a = area_list[0]

    areas = []

    for a in area_list:
        for established_area in areas:
            established_area.add_overlap(a)
        if a.get_parity():
            areas.append(a)
    
    total_area = 0

    for a in areas:
        total_area += a.get_box_area()
        total_area -= get_total_area(a.overlaps)

    return total_area
    

def main():

    begin = time.perf_counter()

    instructions = get_instructions()
    area_list = [area((inst[0], inst[1] + 1), (inst[2], inst[3] + 1), (inst[4], inst[5] + 1), par) for par, inst in instructions]
    tot_a = get_total_area(area_list[0:20])

    instructionsb = get_instructions()
    area_list = [area((inst[0], inst[1] + 1), (inst[2], inst[3] + 1), (inst[4], inst[5] + 1), par) for par, inst in instructions]
    tot_b = get_total_area(area_list)

    print(f"Part A: {tot_a}")
    print(f"Part B: {tot_b}")

    end = time.perf_counter()

    print(f"Total time: {end - begin}")
    

if __name__ == "__main__":
    main()