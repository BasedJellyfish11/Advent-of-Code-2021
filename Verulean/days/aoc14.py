from collections import Counter


fmt_dict = {
    'sep': '\n\n'
    }

class PairwisePolymer:
    def __init__(self, template, rules):
        self._rules = {pair : insert for pair, insert in rules}
        
        self._pair_counts = Counter()
        for i in range(len(template) - 1):
            self._pair_counts[template[i:i+2]] += 1
        
        self._letter_counts = Counter(template)
    
    def _step(self):
        prev_rules, self._pair_counts = self._pair_counts, Counter()
        
        for pair, count in prev_rules.items():
            insert = self._rules[pair]
            self._letter_counts[insert] += count
            self._pair_counts[pair[0]+insert] += count
            self._pair_counts[insert+pair[1]] += count
    
    def _metric(self):
        c = self._letter_counts.values()
        return max(c) - min(c)
    
    def _run(self, n):
        for _ in range(n):
            self._step()
        return self._metric()
    
    def solve(self):
        return self._run(10), self._run(40 - 10)

def solve(data):
    template, rules = data
    rules = [rule.split(' -> ') for rule in rules.split('\n')]
    return PairwisePolymer(template, rules).solve()