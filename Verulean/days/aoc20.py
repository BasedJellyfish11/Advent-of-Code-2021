import numpy as np


fmt_dict = {
    'sep': '\n\n'
    }

def get_next_char(key, image, i, j):
    num = ''
    m, n = image.shape
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            ii = (i+di) % m
            jj = (j+dj) % n
            num += str(int(image[ii, jj]))
    
    num = int(num, 2)
    return key[num]

def solve(data, N=50):
    key = np.array(list(data[0]))
    key = np.where(key == '#', 1, 0)
    
    im0 = [list(line) for line in data[1].split('\n')]
    im0 = np.array(im0)
    im0 = np.where(im0 == '#', 1, 0)
    im0 = np.pad(im0, N)
    
    m, n = im0.shape
    
    for step in range(1,N+1):
        next_im = np.copy(im0)
        for i in range(m):
            for j in range(n):
                next_im[i, j] = get_next_char(key, im0, i, j)
        im0 = next_im
        
        if step == 2:
            ans_a = np.count_nonzero(next_im)

    return ans_a, np.count_nonzero(im0)