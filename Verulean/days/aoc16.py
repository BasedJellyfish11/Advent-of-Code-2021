test = False

def bint(n):
    return int(''.join(n), 2)

hex_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
    }

fmt_dict = {
    'sep': None
    }

if test:
    fmt_dict['file_prefix'] = 'test_'

def header(s):
    version = bint(s[0:3])
    type_ID = bint(s[3:6])
    s[:] = s[6:]
    
    return version, type_ID

def literal(s, offset):
    num = ''
    while s[0] == '1':
        num += ''.join(s[1:5])
        s[:] = s[5:]
        offset = (offset + 5) % 4
    num += ''.join(s[1:5])
    s[:] = s[5:]
    
    # num = num.lstrip('0')
    # offset = (offset + 5) % 4
    
    # if offset:
    #     for _ in range(4 - offset):
    #         s[:] = s[1:]
    
    return int(num, 2), offset

def operator(s):
    if s[0] == '0':
        ID = 0
        n = bint(s[1:16])
        s[:] = s[16:]
    else:
        ID = 1
        n = bint(s[1:12])
        s[:] = s[12:]
    return ID, n

version_sum = 0

class Packet:
    def __init__(self, s, packet_count=None, offset=0):
        self.ver, self.type = header(s)
        offset = (offset + 6) % 4
        
        global version_sum
        version_sum += self.ver
        
        if self.type == 4:
            self.value, offset = literal(s, offset)
        else:
            self.length_ID, self.N = operator(s)
            
            if self.length_ID == 0:
                self.subpackets = []
                new_s = s[:self.N]
                while new_s:
                    self.subpackets.append(Packet(new_s))
                s[:] = s[self.N:]
            else:
                self.subpackets = []
                for _ in range(self.N):
                    self.subpackets.append(Packet(s))
    
    def eval(self):
        if self.type == 4:
            return self.value
        elif self.type == 0: # sum
            return sum(x.eval() for x in self.subpackets)
        elif self.type == 1:
            prod = 1
            for x in self.subpackets:
                prod *= x.eval()
            return prod
        elif self.type == 2:
            return min(x.eval() for x in self.subpackets)
        elif self.type == 3:
            return max(x.eval() for x in self.subpackets)
        elif self.type == 5:
            return int(self.subpackets[0].eval() > self.subpackets[1].eval())
        elif self.type == 6:
            return int(self.subpackets[0].eval() < self.subpackets[1].eval())
        elif self.type == 7:
            return int(self.subpackets[0].eval() == self.subpackets[1].eval())


def solve(data):
    binary_data = ''
    for hex_digit in data:
        binary_data += hex_bin[hex_digit]
    binary_data = list(binary_data)
    
    res = Packet(binary_data)
    
    return version_sum, res.eval()