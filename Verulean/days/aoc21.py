import numpy as np
from collections import defaultdict


def bmod(x, a=1, b=10):
    return (x - a) % (b - a + 1) + a

# Part 1
class DeterministicDie:
    def __init__(self):
        self.rolls = 0
        self.n = 3
    def roll(self):
        triple_sum = sum(bmod(roll, 1, 100) for roll in range(self.n-2, self.n+1))
        self.n += 3
        self.rolls += 3
        return triple_sum

class Player:
    def __init__(self, position):
        self.score = 0
        self.position = position
    def play(self, die):
        roll = die.roll()
        self.position = bmod(self.position + roll)
        self.score += self.position
    def has_won(self):
        return self.score >= 1000

def p1(pos1, pos2):
    p1 = Player(pos1)
    p2 = Player(pos2)
    die = DeterministicDie()
    while True:
        for player in (p1, p2):
            player.play(die)
            if player.has_won():
                return min(p.score for p in (p1, p2)) * die.rolls

# Part 2
class DiracDiceGame:
    dirac_rolls = {(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)}
    
    @staticmethod
    def new_scores():
        return np.zeros((21, 21), dtype=np.uint64)
    
    def __init__(self, p1_pos, p2_pos):
        self.wins = [0, 0]
        
        initial_scores = DiracDiceGame.new_scores()
        initial_scores[0, 0] = 1
        self.multiverse = {(p1_pos, p2_pos) : initial_scores}
    
    def step(self, positions, scores):
        p1_old, p2_old = positions
        for p1_roll, p1_freq in DiracDiceGame.dirac_rolls:
            p1_new = bmod(p1_old + p1_roll)
            scores_p1 = p1_freq * np.roll(scores, p1_new, axis=0)
            self.wins[0] += int(np.sum(scores_p1[:p1_new]))
            scores_p1[:p1_new] = 0
            
            if not np.any(scores_p1):
                continue
            
            for p2_roll, p2_freq in DiracDiceGame.dirac_rolls:
                p2_new = bmod(p2_old + p2_roll)
                scores_p2 = p2_freq * np.roll(scores_p1, p2_new, axis=1)
                self.wins[1] += int(np.sum(scores_p2[:, :p2_new]))
                scores_p2[:, :p2_new] = 0
                
                yield (p1_new, p2_new), scores_p2
    
    def step_multiverse(self):
        next_multiverse = defaultdict(DiracDiceGame.new_scores)
        for old_pos, old_scores in self.multiverse.items():
            for new_pos, new_scores in self.step(old_pos, old_scores):
                next_multiverse[new_pos] += new_scores
        self.multiverse = next_multiverse
    
    def solve(self):
        while self.multiverse:
            self.step_multiverse()
        return max(self.wins)

def solve(data):
    initial_pos = [int(line.split(': ')[-1]) for line in data]
    ans_a = p1(*initial_pos)
    ans_b = DiracDiceGame(*initial_pos).solve()
    return ans_a, ans_b