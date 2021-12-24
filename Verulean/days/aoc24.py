def z_value(w):
    # w = [int(x) for x in str(inputs)]
    
    if 0 in w:
        return 1
    
    z = w[0] + 6
    
    z = 26 * z + w[1] + 2
    
    z = 26 * z + w[2] + 13
    
    z, x = divmod(z, 26)
    if w[3] != (x - 6):
        z = 26 * z + w[3] + 8
    
    z = 26 * z + w[4] + 13
    
    z, x = divmod(z, 26)
    if w[5] != (x - 12):
        z = 26 * z + w[5] + 8
    
    z = 26 * z + w[6] + 3
    
    z = 26 * z + w[7] + 11
    
    z = 26 * z + w[8] + 10
    
    z, x = divmod(z, 26)
    if w[9] != (x - 2):
        z = 26 * z + w[9] + 8
    
    z, x = divmod(z, 26)
    if w[10] != (x - 5):
        z = 26 * z + w[10] + 14
    
    z, x = divmod(z, 26)
    if w[11] != (x - 4):
        z = 26 * z + w[11] + 6
    
    z, x = divmod(z, 26)
    if w[12] != (x - 4):
        z = 26 * z + w[12] + 8
    
    z, x = divmod(z, 26)
    if w[13] != (x - 12):
        z = 26 * z + w[13] + 2
    
    return z

def rirange(a, b, rev):
    if rev:
        return range(b, a-1, -1)
    return range(a, b+1)

def gen_cand(rev=True):
    ad1 = rirange(7, 9, rev)
    ad2 = rirange(3, 9, rev)
    ad3 = rirange(1, 2, rev)
    ad5 = rirange(1, 8, rev)
    ad7 = rirange(2, 9, rev)
    ad8 = rirange(1, 3, rev)
    
    ad9 = rirange(1, 9, rev)
    ad10 = rirange(1, 9, rev)
    
    for d1 in ad1:
        for d2 in ad2:
            for d3 in ad3:
                for d5 in ad5:
                    for d7 in ad7:
                        for d8 in ad8:
                            for d9 in ad9:
                                for d10 in ad10:
                                    yield [d1, d2, d3, d3+7, d5, d5+1, d7, d8, d9, d10, d8+6, d7-1, d2-2, d1-6]

def lint_to_int(l: list):
    return int(''.join(str(d) for d in l))

def solve(_):
    for n in gen_cand():
        if z_value(n) == 0:
            break
    for m in gen_cand(False):
        if z_value(m) == 0:
            break
    return lint_to_int(n), lint_to_int(m)