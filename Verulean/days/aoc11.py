import numpy as np


class FlashingOctopuses:
    def __init__(self, data):
        self._energy = np.array([list(line) for line in data], dtype=int)
        self._flashed = np.zeros_like(self._energy, dtype=bool)
        self._m, self._n = self._energy.shape
        
        # Variables for tracking answers
        self._step_count = 0
        self._total_flashes = 0
    
    def flash(self, i, j):
        # Erroneously, the octopus increases its own energy level as well, but:
        # 1) Basically guaranteed no entries will overflow so who cares
        # 2) Slicing this way is easy and it gets set to 0 at the end anyway
        
        def bounded_slice(a, b, length):
            return slice(max(0, a), min(length, b))
        
        self._energy[
            bounded_slice(i-1, i+2, self._m),
            bounded_slice(j-1, j+2, self._n)
            ] += 1
    
    def step(self):
        self._step_count += 1
        self._flashed.fill(False)
        
        # Increase energy level of all octopuses
        self._energy += 1
        
        # Process flash propagation
        prev_flashes = -1 # lol
        while (curr_flashes := np.count_nonzero(self._flashed)) > prev_flashes:
            prev_flashes = curr_flashes
            
            flash_index = np.nonzero((self._energy > 9) & ~self._flashed)
            for i, j in zip(*flash_index):
                self.flash(i, j)
            
            self._flashed[flash_index] = True
        
        # Reset energy of octopuses that flashed
        self._energy[self._flashed] = 0
        
        self._total_flashes += curr_flashes
    
    def solve(self):
        while not np.all(self._flashed):
            if self._step_count == 100:
                hectostep_flashes = self._total_flashes
            self.step()
        return hectostep_flashes, self._step_count

def solve(data):
    return FlashingOctopuses(data).solve()