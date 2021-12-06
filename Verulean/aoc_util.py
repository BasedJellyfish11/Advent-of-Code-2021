from timeit import timeit


def aoc_input(n, input_dir="input/", cast_type=str, strip=True, sep='\n'):
    with open(f"{input_dir}{n}.txt", 'r') as f:
        return [cast_type(i.strip()) if strip else cast_type(i) for i in f.read().split(sep=sep)]

def time_to_string(n, solve, data):
    units = ((1e0, 's'), (1e-3, 'ms'), (1e-6, 'μs'), (1e-9, 'ns'))
    t = timeit(lambda: solve(data), number=n) / n
    
    for magnitude, unit in units:
        if t > magnitude:
            return f"{t/magnitude:.4f} {unit}"