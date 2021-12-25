from collections import deque
from pprint import pprint
from math import floor, ceil
from itertools import permutations
from functools import reduce
from copy import deepcopy

import json

def parse():
    with open("../input/day18.txt") as f:
        lines = [x.strip() for x in f.readlines()]

    nums = []
    list_nums = []
    for line in lines:
        # we do a small amount of trolling
        list_nums.append(json.loads(line))
        nums.append(to_tree(list_nums[-1]))

    return list_nums, nums

debug = False
def dprint(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def sn_add(a, b):
    res = Node(left=a, right=b)

    a.parent = res
    b.parent = res

    reduce_sn(res)

    return res

def explode(num, depth=0):
    if num.value is not None:
        return False

    if depth < 4:
        return explode(num.left, depth + 1) or explode(num.right, depth + 1)

    l = left_num(num.left)
    r = right_num(num.right)

    if num.parent.left == num:
        num.parent.left = Node(value=0, parent=num.parent)
    else:
        num.parent.right = Node(value=0, parent=num.parent)

    return True

def split(num):
    if num.value is None:
        return split(num.left) or split(num.right)

    if num.value < 10:
        return False

    div_2 = num.value / 2
    num.left = Node(value=floor(div_2), parent=num)
    num.right = Node(value=ceil(div_2), parent=num)
    num.value = None

    return True


class Node:
    def __init__(self, value=None, left=None, right=None, parent=None):
        if value is not None:
            assert left is None and right is None
        else:
            assert value is None

        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        if self.value is not None:
            return f"<{self.value}>"
        else:
            return f"(Node: [{self.left}, {self.right}])"

    def __deepcopy__(self, memo_dict={}):
        res = Node()
        memo_dict[id(self)] = res
        res.value = self.value
        res.left = deepcopy(self.left, memo_dict)
        res.right = deepcopy(self.right, memo_dict)
        res.parent = deepcopy(self.parent, memo_dict)

        return res

def to_tree(num, parent=None):
    if isinstance(num, int):
        return Node(value=num, parent=parent)

    a, b = num

    n = Node(parent=parent)
    n.left = to_tree(a, n)
    n.right = to_tree(b, n)

    return n

def left_num(node):
    prev = node
    n = node.parent

    while n and n.left == prev:
        prev = n
        n = n.parent

    if n is None:
        return None

    if n.right == prev:
        n = n.left

    while n.right is not None:
        n = n.right

    n.value += node.value

def right_num(node):
    prev = node
    n = node.parent

    while n and n.right == prev:
        prev = n
        n = n.parent

    if n is None:
        return 

    if n.left == prev:
        n = n.right

    while n.left is not None:
        n = n.left

    n.value += node.value

def reduce_sn(num):
    while True:
        if explode(num):
            continue

        if split(num):
            continue

        break

def list_tree(t):
    if t.value is not None:
        return t.value

    return [list_tree(t.left), list_tree(t.right)]

def mag(t):
    if t.value is not None:
        return t.value

    return 3 * mag(t.left) + 2 * mag(t.right)

nums = parse()

def solve(nums):
    lnums, nums = nums

    print(mag(reduce(sn_add, nums)))

    maximum = -float('inf')
    for a, b in permutations(lnums, 2):
        # sn_add mutates due to reduction, so use the original lists
        a, b = to_tree(a), to_tree(b)

        maximum = max(maximum, mag(sn_add(a, b)))

    print(maximum)

if __name__ == "__main__":
    solve(parse())
