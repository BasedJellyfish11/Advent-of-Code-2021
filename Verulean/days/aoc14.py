from collections import defaultdict


fmt_dict = {
    'sep': '\n\n'
    }

# fmt_dict['test'] = True

def pairs(s):
    for i in range(len(s)-1):
        yield s[i:i+2]

def new_pairs(old_pair, insert_char):
    return old_pair[0] + insert_char, insert_char + old_pair[1]

def solve(data):
    start, rules = data
    rules = [rule.split(' -> ') for rule in rules.split('\n')]
    rules = {a:b for a, b in rules}
    
    rule_counts = defaultdict(int)
    for pair in pairs(start):
        if pair in rules:
            rule_counts[pair] += 1
    
    letter_counts = defaultdict(int)
    for c in start:
        letter_counts[c] += 1
    
    for i in range(40):
        if i == 10:
            c = letter_counts.values()
            ans_a = max(c) - min(c)
        old_rules = rule_counts
        rule_counts = defaultdict(int)
        for pair, count in old_rules.items():
            for new_pair in new_pairs(pair, rules[pair]):
                rule_counts[new_pair] += count
            letter_counts[rules[pair]] += count
    
    c = letter_counts.values()
    ans_b = max(c) - min(c)
    return ans_a, ans_b