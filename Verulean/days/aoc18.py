class SnailfishNumber:
    @staticmethod
    def pair_elements(pair):
        pair = pair[1:-1]
        depth = 0
        for i, c in enumerate(pair):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            
            if depth == 0:
                while pair[i+1] != ',':
                    i += 1
                return pair[:i+1], pair[i+2:]
    
    def __init__(self, number, depth=0, parent=None, position=None):
        self._depth = depth
        self._parent = parent
        self._pos = position
        self._left = None
        self._right = None
        
        if '[' not in number:
            self._type = 0
            self._value = int(number)
        else:
            self._type = 1
            l, r = SnailfishNumber.pair_elements(number)
            
            self._left = SnailfishNumber(
                l, 
                depth = self._depth + 1, 
                parent = self, 
                position = 0
                )
            
            self._right = SnailfishNumber(
                r, 
                depth = self._depth + 1, 
                parent = self, 
                position = 1
                )
    
    def __str__(self):
        if self._type == 0:
            return str(self._value)
        return f"[{self._left},{self._right}]"
    
    def magnitude(self):
        if self._type == 0:
            return self._value
        return 3 * self._left.magnitude() + 2 * self._right.magnitude()
    
    def _split(self):
        if self._type == 1:
            if self._left._split():
                return True
            if self._right._split():
                return True
        
        if self._type == 0 and self._value >= 10:
            self._type = 1
            l = self._value // 2
            r = l + (self._value % 2)
            
            self._left = SnailfishNumber(
                str(l), 
                depth = self._depth + 1, 
                parent = self, 
                position = 0
                )
            
            self._right = SnailfishNumber(
                str(r),
                depth = self._depth + 1,
                parent = self,
                position = 1
                )
            
            return True
        
        return False
    
    def _extreme_radd(self, n):
        if self._right._type == 0:
            self._right._value += n
        else:
            self._right._extreme_radd(n)
    
    def _extreme_ladd(self, n):
        if self._left._type == 0:
            self._left._value += n
        else:
            self._left._extreme_ladd(n)
    
    def _radd(self, n, caller_position, cascade=False):
        if caller_position == 0:
            if self._right._type == 0:
                self._right._value += n
            elif cascade:
                self._right._extreme_ladd(n)
            else:
                self._right._ladd(n, 1, True)
        elif self._parent is not None:
            self._parent._radd(n, self._pos, True)
    
    def _ladd(self, n, caller_position, cascade=False):
        if caller_position == 1:
            if self._left._type == 0:
                self._left._value += n
            elif cascade:
                self._left._extreme_radd(n)
            else:
                self._left._radd(n, 0, True)
        elif self._parent is not None:
            self._parent._ladd(n, self._pos, True)
    
    def _explode(self):
        if self._type == 1:
            if self._left._explode():
                return True
            if self._right._explode():
                return True
        
        if self._type == 1 \
            and self._depth == 4 \
            and self._left._type == 0 \
            and self._right._type == 0:
                self._parent._ladd(self._left._value, self._pos)
                self._parent._radd(self._right._value, self._pos)
                
                self._type = 0
                self._value = 0
                
                return True
        
        return False
    
    def reduce(self):
        while self._explode() or self._split():
            pass
    
    def __add__(self, other):
        result = SnailfishNumber(f"[{self},{other}]")
        result.reduce()
        return result

def solve(numbers):
    numbers = [SnailfishNumber(x) for x in numbers]
    
    snail_sum = numbers[0]
    for next_num in numbers[1:]:
        snail_sum += next_num
    ans_a = snail_sum.magnitude()
    
    ans_b = 0
    for x in numbers:
        for y in numbers:
            if x is not y:
                ans_b = max(ans_b, (x+y).magnitude())
    
    return ans_a, ans_b