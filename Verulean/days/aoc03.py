import numpy as np


def to_decimal(b):
    d = 0
    for power, digit in enumerate(reversed(b)):
        d += digit * 2 ** power
    return d

def most_common(x: np.ndarray):
    return 2 * np.sum(x, axis=0) >= len(x)

def least_common(x: np.ndarray):
    return ~most_common(x)

def filter_report(f, x):
    i = 0
    while len(x) > 1:
        x = x[x[:,i] == f(x)[i]]
        i += 1
    return to_decimal(x[0])

def solve(x):    
    # Convert input to a 2D Boolean array
    diagnostic_report = np.zeros((len(x), len(x[0])), dtype=bool)
    for i, num in enumerate(x):
        diagnostic_report[i] = [digit == '1' for digit in num]
    
    # Part 1
    gamma = to_decimal(most_common(diagnostic_report))
    epsilon = to_decimal(least_common(diagnostic_report))
    
    # Part 2
    o2_rating = filter_report(most_common, diagnostic_report)
    co2_rating = filter_report(least_common, diagnostic_report)
    
    return gamma * epsilon, o2_rating * co2_rating