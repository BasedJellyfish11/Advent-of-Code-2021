from collections import deque
from itertools import product


fmt_dict = {'sep': 'inp w\n'}

def rirange(a, b, rev):
    """Reversible inclusive range."""
    if rev:
        return range(b, a - 1, -1)
    return range(a, b + 1)

class MONAD:    
    def __init__(self, blocks):
        self._blocks = tuple(type(self).parse_block(block) for block in blocks)
        self._relations = self._digit_relations()
        self._N = len(self._blocks)
    
    @staticmethod
    def parse_block(block):
        grow = (block[3][-1] == '1')
        offset_1 = int(block[4][-1])
        offset_2 = int(block[14][-1])
        return grow, offset_1, offset_2
    
    def _digit_relations(self):
        r = {}
        q = deque()
        for digit, (grow, o1, o2) in enumerate(self._blocks):
            if grow:
                q.append((digit, o2))
            else:
                check_digit, check_offset = q.pop()
                r[digit] = (check_digit, check_offset + o1)
        return r
    
    def _candidates(self, rev=True):
        fixed = self._digit_relations()
        free = {}
        
        # Bound possible values of free digits
        for digit, offset in fixed.values():
            if offset > 0:
                bounds = (1, 9 - offset)
            else:
                bounds = (1 - offset, 9)
            free[digit] = rirange(*bounds, rev)
        
        # Add in any unrepresented digits as free variables
        for digit in range(self._N):
            if (digit not in fixed) and (digit not in free):
                free[digit] = rirange(1, 9, rev)
        
        for free_digits in product(*free.values()):
            n = {}
            for i, value in zip(free, free_digits):
                n[i] = value
            for i, (source, offset) in fixed.items():
                n[i] = n[source] + offset
            yield [n[i] for i in range(self._N)]
    
    def _run_block(self, block_index, z, w):
        g, o1, o2 = self._blocks[block_index]
        x = (z % 26 + o1) != w
        if not g:
            z //= 26
        if x:
            z = 26 * z + w + o2
        return z
    
    def _run(self, number: list):
        z = 0
        for i, w in enumerate(number):
            z = self._run_block(i, z, w)
        return z
    
    def _first_valid(self, rev=True):
        for n in self._candidates(rev=rev):
            if self._run(n) == 0:
                break
        result = 0
        for power, digit in enumerate(reversed(n)):
            result += digit * 10 ** power
        return result
    
    def solve(self):
        return self._first_valid(), self._first_valid(rev=False)

def solve(data):
    blocks = [[instr.split() for instr in block.split('\n')] for block in data if block]
    return MONAD(blocks).solve()