def read_file(path: str, cast_type=str, strip=True):
    with open(path, 'r') as f:
        return [cast_type(i.strip()) for i in f.readlines()]

def aoc_input(n, input_dir="input/", cast_type=str, strip=True):
    return read_file(f"{input_dir}{n}.txt", cast_type=cast_type, strip=strip)