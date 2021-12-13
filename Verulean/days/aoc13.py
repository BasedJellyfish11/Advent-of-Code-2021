import numpy as np


fmt_dict = {
    'sep': '\n\n',
    }

class TransparencyOrigami:
    def __init__(self, points, folds):
        self._points = np.array([coord.split(',') for coord in points], dtype=int)
        
        folds = [instr[11:].split('=') for instr in folds]
        self._folds = tuple(
            (0 if axis == 'x' else 1, int(index)) 
            for axis, index in folds
            )
    
    def to_string(self, fg='#', bg=' ', bounds=(40,6)):
        points = {(x, y) for x, y in self._points}
        result = ""
        for y in range(bounds[1]):
            for x in range(bounds[0]):
                if (x, y) in points:
                    result += fg
                else:
                    result += bg
            result += '\n'
        return result
    
    def _fold(self, axis, index):
        fold_index = (self._points[:, axis] > index, axis)
        self._points[fold_index] = 2 * index - self._points[fold_index]
    
    def solve(self):
        self._fold(*self._folds[0])
        first_fold_dots = len(np.unique(self._points, axis=0))
        
        for axis, index in self._folds[1:]:
            self._fold(axis, index)
        
        return first_fold_dots, self.to_string()

def solve(data):
    points, folds = map(lambda s: s.split('\n'), data)
    return TransparencyOrigami(points, folds).solve()