from datetime import datetime as dt
from importlib import import_module
import aoc_util


def main(n=dt.today().day, time_solution=False, n_trials=1000):
    aoc = import_module(f"days.aoc{n}")
    fmt = getattr(aoc, 'fmt_dict', {})
    
    data = aoc_util.aoc_input(n, **fmt)
    
    if time_solution:
        print(f"Day {n} solution averaged {aoc_util.time_to_string(n_trials, aoc.solve, data)} over {n_trials} runs.")
    else:
        print(aoc.solve(data))


if __name__ == '__main__':
    main()