import numpy as np


class SmokeBasin:
    def __init__(self, data):
        self._height = np.array([list(row) for row in data], dtype=int)
        self._expand = self._height < np.amax(self._height)
        self._m, self._n = self._height.shape
    
    def _low_points(self):
        compare = ((1, 0), (-1, -1))
        
        low = np.ones_like(self._height, dtype=bool)
        clear_value = np.amax(self._height) + 1
        for axis in (0, 1):
            for offset, clear_index in compare:
                shifted = np.roll(self._height, offset, axis=axis)
                if axis == 0:
                    shifted[clear_index] = clear_value
                elif axis == 1:
                    shifted[:, clear_index] = clear_value
                low &= self._height < shifted
        
        return np.nonzero(low)
    
    # Shoutouts to 56
    def _basin_size(self, i, j):
        positions = set()
        
        def fill(x, y):
            def try_pos(position):
                px, py = position
                if self._expand[position] and position not in positions:
                    positions.add(position)
                    fill(px, py)
            if x - 1 >= 0:
                try_pos((x-1, y))
            if x + 1 < self._m:
                try_pos((x+1, y))
            if y - 1 >= 0:
                try_pos((x, y-1))
            if y + 1 < self._n:
                try_pos((x, y+1))
        
        fill(i, j)
        return len(positions)
    
    def solve(self):
        # Part 1
        low = self._low_points()
        ans_a = np.sum(self._height[low] + 1)
        
        # Part 2
        basin_sizes = np.zeros_like(low[0], dtype=int)
        for i, (i_low, J_Lo) in enumerate(zip(*low)):
            basin_sizes[i] = self._basin_size(i_low, J_Lo)
        ans_b = np.prod(np.sort(basin_sizes)[-3:])
        
        return ans_a, ans_b


def solve(data):
    big_smoke = SmokeBasin(data)
    return big_smoke.solve()