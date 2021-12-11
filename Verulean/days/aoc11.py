import numpy as np


n_steps = 100

def flash_count(data):
    return np.count_nonzero(data > 9)

def flashes(data):
    return np.nonzero(data > 9)

def adjacents(i, j):
    m, n = 10, 10
    candidates = ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
    
    for x, y in candidates:
        if 0 <= x < m and 0 <= y < n:
            yield x, y

def solve(data):
    data = np.array([list(i) for i in data], dtype=int)
    flash = np.zeros_like(data, dtype=bool)
    
    FLASH_SUM = 0
    
    step = 0
    while np.count_nonzero(flash) != 100:
        step += 1
        data += 1
        
        flash.fill(False)
        
        X = np.count_nonzero(flash)
        
        df = 1
        while df > 0:
            i_flash = flashes(data)
            for i, j in zip(*i_flash):
                if not flash[i,j]:
                    for i2, j2 in adjacents(i, j):
                        data[i2, j2] += 1
            
            flash[i_flash] = True
            Y = np.count_nonzero(flash)
            df, X = Y - X, Y
        
        data[flash] = 0
        FLASH_SUM += np.count_nonzero(flash)
        
        if step == 100:
            ans_a = FLASH_SUM
    return ans_a, step