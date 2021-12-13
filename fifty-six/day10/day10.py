with open("../input/day10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

score_p1 = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
}

score_p2 = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
}

rev = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<'
}

rev_left = { y: x for (x, y) in rev.items() }

left = set(rev.values())
right = set(rev.keys())

def solve():
    p1_total = 0
    p2_scores = []
    for line in lines:
        q = []
        for char in line:
            if char in left:
                q.append(char)
            elif char in right:
                if q[-1] != rev[char]:
                    p1_total += score_p1[char]
                    break
                else:
                    q.pop()
        else:
            line_score = 0
    
            while q:
                c = q.pop()
                line_score *= 5
                line_score += score_p2[rev_left[c]]
    
            p2_scores.append(line_score)
    
    p2_scores.sort()
    return p1_total, p2_scores[len(p2_scores) // 2]

if __name__ == "__main__":
    p1, p2 = solve()
    print("p1: ", p1)
    print("p2: ", p2)
