class SnailfishNumber:
    def __init__(self, number, depth=0, parent=None, position=None):
        self._master = number
        self._depth = depth
        self._parent = parent
        self._pos = position
        self._children = [None, None]
        
        if isinstance(number, int):
            self._type = 0
            self._value = number
        else:
            self._type = 1
            for i in range(2):
                self._children[i] = SnailfishNumber(number[i], depth=self._depth+1, parent=self, position=i)
    
    def __str__(self):
        if self._type == 0:
            return str(self._value)
        return f"[{self._children[0]},{self._children[1]}]"
    
    def __add__(self, other):
        result = SnailfishNumber([self._master, other._master])
        result._reduce()
        return result
    
    def _recompute_master(self):
        if self._type == 0:
            return self._value
        return [self._children[0]._recompute_master(), self._children[1]._recompute_master()]
    
    def _edge_add(self, n, position):
        if self._children[position]._type == 0:
            self._children[position]._value += n
        else:
            self._children[position]._edge_add(n, position)
    
    def _adj_add(self, n, target_position, caller_position):
        if caller_position != target_position:
            if self._children[target_position]._type == 0:
                self._children[target_position]._value += n
            else:
                self._children[target_position]._edge_add(n, 1-target_position)
        elif self._parent is not None:
            self._parent._adj_add(n, target_position, self._pos)
    
    def _split(self):
        if self._type == 1 and (self._children[0]._split() or self._children[1]._split()):
            return True
        
        if self._type == 0 and self._value >= 10:
            self._type = 1
            
            split_nums = [self._value // 2, self._value // 2 + self._value % 2]
            
            for i in range(2):
                self._children[i] = SnailfishNumber(split_nums[i], depth=self._depth+1, parent=self, position=i)
            
            return True
        
        return False
    
    def _explode(self):
        if self._type == 1 and (self._children[0]._explode() or self._children[1]._explode()):
            return True
        
        if self._type == 1 \
            and self._depth >= 4 \
            and self._children[0]._type == 0 \
            and self._children[1]._type == 0:
                for i in range(2):
                    self._parent._adj_add(self._children[i]._value, i, self._pos)
                self._type = 0
                self._value = 0
                
                return True
        
        return False
    
    def _reduce(self):
        while self._explode() or self._split():
            pass
        self._master = self._recompute_master()
    
    def magnitude(self):
        if self._type == 0:
            return self._value
        return 3 * self._children[0].magnitude() + 2 * self._children[1].magnitude()

def solve(data):
    nums = [SnailfishNumber(eval(x)) for x in data]
    
    ans_a = sum(nums[1:], start=nums[0]).magnitude()
    ans_b = max((x+y).magnitude() for x in nums for y in nums if x is not y)
    
    return ans_a, ans_b