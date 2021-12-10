from datetime import datetime as dt
from importlib import import_module
import aoc_util


def main(n=dt.today().day, time=False, n_trials=1000):
    aoc = import_module(f"days.aoc{n:02}")
    fmt = getattr(aoc, 'fmt_dict', {})
    data = aoc_util.aoc_input(f"{n:02}.txt", **fmt)
    
    if time:
        t = aoc_util.time_to_string(n_trials, aoc.solve, data)
        print(f"Day {n}: average of {t} over {n_trials} runs.")
    
    solution = aoc.solve(data)
    print(solution)
    return solution

if __name__ == '__main__':
    x = main()