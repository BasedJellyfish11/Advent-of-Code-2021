fmt_dict = {
    'sep': '\n'
    }

def get_pairs(n):
    nest = 0
    n = n[1:-1]
    pairs = []
    for i, c in enumerate(n):
        if c == '[':
            nest += 1
        elif c == ']':
            nest -= 1
        
        if nest == 0:
            pairs.append(n[:i+1])
            pairs.append(n[i+1:].lstrip(','))
            return pairs

class Number:
    def __init__(self, number, rec=0, parent=None, pos=None):
        self.rec = rec
        self.parent = parent
        self.pos = pos
        
        self.left = None
        self.right = None
        
        if '[' not in number:
            self.type = 0
            self.value = int(number)
        else:
            self.type = 1
            l, r = get_pairs(number)
            self.left = Number(l, rec=self.rec+1, parent=self, pos='l')
            self.right = Number(r, rec=self.rec+1, parent=self, pos='r')
        
        # self.reduce()
    
    @classmethod
    def from_children(cls, left, right):
        x = cls('0')
        x.left = left
        x.right = right
        x.type = 1
        
        x.left.parent = x
        x.right.parent = x
        x.left.pos = 'l'
        x.right.pos = 'r'
        return x
    
    def __str__(self):
        if self.type == 0:
            return str(self.value)
        else:
            return f"[{self.left},{self.right}]"
    
    def nest(self):
        self.rec += 1
        if self.type == 1:
            for child in (self.left, self.right):
                child.nest()
    
    def magnitude(self):
        if self.type == 0:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def split(self):
        # print(f"splitting {self}")
        if self.type == 1:
            if self.left.split():
                return True
            if self.right.split():
                return True
        
        if self.type == 0 and self.value >= 10:
            self.type = 1
            l = self.value // 2
            if self.value % 2 == 0:
                r = l
            else:
                r = l + 1
            self.left = Number(str(l), rec=self.rec+1, parent=self, pos='l')
            self.right = Number(str(r), rec=self.rec+1, parent=self, pos='r')
            return True
        
        return False
    
    def extreme_r_add(self, n):
        if self.right.type == 0:
            self.right.value += n
        else:
            self.right.extreme_r_add(n)
    
    def extreme_l_add(self, n):
        if self.left.type == 0:
            self.left.value += n
        else:
            self.left.extreme_l_add(n)
    
    # def r_add(self, n, call_pos, sideline=False):
    #     # print(self)
    #     if call_pos == 'l':
    #         if self.right.type == 0:
    #             self.right.value += n
    #         elif sideline:
    #             self.right.r_add(n, 'r', True)
    #         else:
    #             self.right.l_add(n, 'r', True)
    #     elif self.parent is not None:
    #         self.parent.r_add(n, self.pos)
    
    def r_add(self, n, call_pos, cascade=False):
        if call_pos == 'l':
            if self.right.type == 0:
                self.right.value += n
            elif cascade:
                self.right.extreme_l_add(n)
            else:
                self.right.l_add(n, 'r', True)
        elif self.parent is not None:
            self.parent.r_add(n, self.pos, True)
    
    def l_add(self, n, call_pos, cascade=False):
        if call_pos == 'r':
            if self.left.type == 0:
                self.left.value += n
            elif cascade:
                self.left.extreme_r_add(n)
            else:
                self.left.r_add(n, 'l', True)
        elif self.parent is not None:
            self.parent.l_add(n, self.pos, True)
    
    def explode(self):
        # print(f"exploding {self}")
        if self.type == 1:
            if self.left.explode():
                return True
            if self.right.explode():
                return True
            
        if self.type == 1 and self.rec == 4 and self.left.type == 0 and self.right.type == 0:
            self.parent.l_add(self.left.value, self.pos)
            self.parent.r_add(self.right.value, self.pos)
            self.type = 0
            self.value = 0
            return True
        
        return False
    
    def reduce(self):
        while True:
            # if self.rec == 0:
            #     print(self)
            if self.explode():
                continue
            if self.split():
                continue
            break
        return self
    
    def __mul__(self, other):
        num_sum = Number(f"[{self},{other}]")
        # self.nest()
        # other.nest()
        # num_sum = Number.from_children(self, other)
        return num_sum

def solve(data):
    # x = Number(data[0])
    # x.reduce()
    # for s in data[1:]:
    #     y = Number(s)
    #     x = x + Number(s)
    #     print(x.magnitude())
    
    
    x = Number(data[0])
    # x.reduce()
    # i = 1
    for next_num_str in data[1:]:
        # y = Number(next_num_str)
        # y.reduce()
        x = x * Number(next_num_str)
        # print(x)
        x.reduce()
    # print(x)
    ans_a = x.magnitude()
    
    
    max_magnitude = 0
    for i, x in enumerate(data):
        for j, y in enumerate(data):
            if i != j:
                snail_sum = Number(x) * Number(y)
                snail_sum.reduce()
                max_magnitude = max(max_magnitude, snail_sum.magnitude())
    ans_b = max_magnitude
    return ans_a, ans_b

# if __name__ == '__main__':
#     t = [f"[{i},{i}]" for i in range(1, 7)]
#     x = Number(t[0])
#     for s in t[1:]:
#         y = Number(s)
#         x = x * y
#     print(x)