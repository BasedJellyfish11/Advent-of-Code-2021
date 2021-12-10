from collections import defaultdict


def solve(data):
    segments = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    snowflakes = {
        42: '0',
        17: '1',
        34: '2',
        39: '3',
        30: '4',
        37: '5',
        41: '6',
        25: '7',
        49: '8',
        45: '9',
        }

    freq = defaultdict(int)
    decoded_output = [0] * len(data)

    for i, line in enumerate(data):
        freq.clear()
        tests, raw_output = line.split(' | ')
        raw_output = raw_output.split()

        for c in segments:
            freq[c] += tests.count(c)

        decoded_output[i] = ''.join(
            snowflakes[sum(freq[c] for c in signal)] 
            for signal in raw_output
            )

    s = ''.join(decoded_output)
    ans_a = sum(s.count(d) for d in ('1', '4', '7', '8'))
    ans_b = sum(int(n) for n in decoded_output)
    
    return ans_a, ans_b