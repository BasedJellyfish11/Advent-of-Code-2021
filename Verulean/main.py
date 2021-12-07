from datetime import datetime as dt
from importlib import import_module
import aoc_util


def main(n=dt.today().day, time=False, n_trials=1000):
    aoc = import_module(f"days.aoc{n}")
    fmt = getattr(aoc, 'fmt_dict', {})
    
    data = aoc_util.aoc_input(n, **fmt)
    
    if time:
        print(f"Day {n} solution averaged {aoc_util.time_to_string(n_trials, aoc.solve, data)} over {n_trials} runs.")
    print(aoc.solve(data))


if __name__ == '__main__':
    main()