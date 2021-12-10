import numpy as np


fmt_dict = {
    'sep': ',',
    'cast_type': int
    }

def solve(data, day_targets=(80, 256)):
    initial_population = np.array(data, dtype=int)
    age_counts = np.array([np.sum(initial_population == i) for i in range(9)], dtype=np.uint64)
    
    result = {day:0 for day in day_targets}
    for day in range(1, max(day_targets)+1):
        age_counts = np.roll(age_counts, -1)
        age_counts[6] += age_counts[-1]
        if day in result:
            result[day] = np.sum(age_counts)

    return tuple(result[day] for day in day_targets)