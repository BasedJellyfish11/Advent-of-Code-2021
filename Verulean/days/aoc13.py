import numpy as np
from collections import defaultdict, deque

fmt_dict = {
    'sep': '\n\n',
    }

# fmt_dict['test'] = True

def fold(paper, axis, index):
    m, n = paper.shape
    if axis == 0:
        bottom = paper[:index]
        m2, n2 = bottom.shape
        top = np.flipud(paper[index+1:])
        m3, n3 = top.shape
        if m2 > m3:
            top = np.append(np.zeros((m2 - m3, n), dtype=bool), top, axis=axis)
            print(0)
        elif m3 > m2:
            bottom = np.append(np.zeros((m3 - m2, n), dtype=bool), bottom, axis=axis)
            print(1)
    else:
        bottom = paper[:, :index]
        m2, n2 = bottom.shape
        top = np.fliplr(paper[:, index+1:])
        m3, n3 = top.shape
        if n2 > n3:
            top = np.append(np.zeros((m, n2 - n3), dtype=bool), top, axis=axis)
            print(2)
        elif n3 > n2:
            bottom = np.append(np.zeros((m, n3 - n2), dtype=bool), bottom, axis=axis)
            print(3)
    
    return (bottom | top)

def print_sheet(paper, fg='#', bg=' '):
    p = np.where(paper, fg, bg)
    for row in p:
        print(''.join(row))

def solve(data):
    points, instructions = data
    points = points.split('\n')
    points = [coord.split(',') for coord in points]
    instructions = instructions.split('\n')
    instructions = [ins[11:].split('=') for ins in instructions]
    
    points = np.array(points, dtype=int)
    n, m = np.amax(points, axis=0) + 1
    
    paper = np.zeros((m, n), dtype=bool)
    paper[(points[:,1], points[:,0])] = True
    
    axis_dict = {'y':0, 'x':1}
    
    for i, (axis, index) in enumerate(instructions):
        m, n = paper.shape
        index = int(index)
        if axis == 0:
            print(m, index, m/index)
        else:
            print(n, index, n/index)
        paper = fold(paper, axis_dict[axis], index)
        # if i == 0:
        #     print(np.count_nonzero(paper))
    print_sheet(paper)
    return paper
