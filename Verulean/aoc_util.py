def aoc_input(n, input_dir="input/", cast_type=str, strip=True, sep='\n'):
    with open(f"{input_dir}{n}.txt", 'r') as f:
        return [cast_type(i.strip()) if strip else cast_type(i) for i in f.read().split(sep=sep)]