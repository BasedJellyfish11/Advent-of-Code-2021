from collections import deque
from enum import Enum


class SyntaxScore:
    pairs = {'(':')', '[':']', '{':'}', '<':'>'}
    
    class SubSyntaxError(Enum):
        ALL_CLEAR = 0
        BAD_CLOSE = 1
        INCOMPLET = 2
    
    def __init__(self, data):
        self._data = data
    
    def get_error(self, line):
        q = deque()
        for char in line:
            if char in self.pairs:
                q.appendleft(self.pairs[char])
            elif char == q[0]:
                q.popleft()
            else: # Incorrect closing character
                return (self.SubSyntaxError.BAD_CLOSE, char)
            
        if q: # Incomplete line
            return (self.SubSyntaxError.INCOMPLET, q)
        
        else: # No syntax errors
            return (self.SubSyntaxError.ALL_CLEAR, None)
    
    def error_score(self, line):
        error, offender = self.get_error(line)
        if error == self.SubSyntaxError.ALL_CLEAR:
            score = 0
        
        elif error == self.SubSyntaxError.BAD_CLOSE:
            scores = {
                ')': 3, 
                ']': 57, 
                '}': 1197, 
                '>': 25137,
                }
            score = scores[offender]
        
        elif error == self.SubSyntaxError.INCOMPLET:
            scores = {
                ')': 1, 
                ']': 2, 
                '}': 3, 
                '>': 4,
                }
            score = 0
            for c in offender:
                score = 5 * score + scores[c]
        
        return (error, score)
    
    def solve(self):
        ans_a = 0
        scores_b = []
        
        for line in self._data:
            err, score = self.error_score(line)
            if err == self.SubSyntaxError.BAD_CLOSE:
                ans_a += score
            elif err == self.SubSyntaxError.INCOMPLET:
                scores_b.append(score)
        
        ans_b = sorted(scores_b)[len(scores_b) // 2]
        return ans_a, ans_b

def solve(data):
    return SyntaxScore(data).solve()