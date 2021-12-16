fmt_dict = {
    'sep': None,
    }

def bint(n):
    return int(n, 2)

class BitView:
    def __init__(self, binary_string):
        self._bits = binary_string
        self._index = 0
    
    def __len__(self):
        return len(self._bits[self._index:])
    
    def get(self, bit_count):
        view = self._bits[self._index:self._index + bit_count]
        self._index += bit_count
        return view
    
    def get_subview(self, bit_count):
        return type(self)(self.get(bit_count))

class BITSParser(BitView):
    @classmethod
    def from_hex(cls, transmission):
        bits = ''
        for hex_digit in transmission:
            bits += bin(int(hex_digit, 16))[2:].zfill(4)
        
        return cls(bits)
    
    def header(self):
        version = bint(self.get(3))
        type_id = bint(self.get(3))
        
        return version, type_id
    
    def literal(self):
        num = ''
        
        block = self.get(5)
        while block[0] == '1':
            num += block[1:]
            block = self.get(5)
        num += block[1:]
        
        return bint(num)
    
    def operator(self):
        length_id = self.get(1)
        if length_id == '0':
            n = self.get(15)
        else:
            n = self.get(11)
            
        return length_id, bint(n)

class BITSPacket:
    def __init__(self, bits: BITSParser):
        self.version, self.type = bits.header()
        self.subpackets = []
        
        if self.type == 4: # Literal value
            self.value = bits.literal()
        
        else: # Operator
            self.length_id, self.N = bits.operator()
            
            if self.length_id == '0':
                # Specified number of bits
                bit_window = bits.get_subview(self.N)
                while bit_window:
                    self.subpackets.append(type(self)(bit_window))
            else:
                # Specified number of subpackets
                for _ in range(self.N):
                    self.subpackets.append(type(self)(bits))
    
    def version_sum(self):
        return self.version + sum(sub.version_sum() for sub in self.subpackets)
    
    def eval(self):
        # Python 3.9 so no match case woooooooooooooooooooooooooooooo
        if self.type == 0:
            return sum(sub.eval() for sub in self.subpackets)
        elif self.type == 1:
            prod = 1
            for sub in self.subpackets:
                prod *= sub.eval()
            return prod
        elif self.type == 2:
            return min(sub.eval() for sub in self.subpackets)
        elif self.type == 3:
            return max(sub.eval() for sub in self.subpackets)
        elif self.type == 4:
            return self.value
        elif self.type == 5:
            return int(self.subpackets[0].eval() > self.subpackets[1].eval())
        elif self.type == 6:
            return int(self.subpackets[0].eval() < self.subpackets[1].eval())
        elif self.type == 7:
            return int(self.subpackets[0].eval() == self.subpackets[1].eval())

def solve(data):
    bits = BITSParser.from_hex(data)
    parsed_packet = BITSPacket(bits)
    return parsed_packet.version_sum(), parsed_packet.eval()