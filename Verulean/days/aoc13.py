import numpy as np


fmt_dict = {
    'sep': '\n\n',
    }

class TransparencyOrigami:
    def __init__(self, points, folds):
        points = np.array([coord.split(',') for coord in points], dtype=int)
        folds = [instr[11:].split('=') for instr in folds]
        
        n, m = np.amax(points, axis=0) + 1
        self._paper = np.zeros((m, n), dtype=bool)
        self._paper[(points[:,1], points[:,0])] = True
        
        self._folds = tuple(
            (1 if axis == 'x' else 0, int(index)) 
            for axis, index in folds
            )
    
    def to_string(self, fg='#', bg=' '):
        p = np.where(self._paper, fg, bg)
        return '\n'.join(''.join(row) for row in p)
    
    def _fold(self, axis, index):
        bottom, _, top = np.split(self._paper, [index, index+1], axis=axis)
        
        m_b, n_b = bottom.shape
        m_t, n_t = top.shape
        M, N = max(m_b, m_t), max(n_b, n_t)
        self._paper = np.zeros((M, N), dtype=bool)
        
        if axis == 0:
            self._paper[:m_b] |= bottom
            self._paper[-1:-(m_t+1):-1] |= top
        elif axis == 1:
            self._paper[:, :n_b] |= bottom
            self._paper[:, -1:-(n_t+1):-1] |= top
    
    def solve(self):
        self._fold(*self._folds[0])
        first_fold_dots = np.count_nonzero(self._paper)
        
        for axis, index in self._folds[1:]:
            self._fold(axis, index)
        
        return first_fold_dots, self.to_string()

def solve(data):
    points, folds = map(lambda s: s.split('\n'), data)
    return TransparencyOrigami(points, folds).solve()