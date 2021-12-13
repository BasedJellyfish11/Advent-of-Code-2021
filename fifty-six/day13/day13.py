from pprint import pprint

test = False

class TransparentPaper:
    def __init__(self):
        folds = []
        points = set()

        with open(f"../input/{'test_' if test else ''}day13.txt") as f:
            for line in f:
                if not line.strip():
                    continue
        
                if line.startswith("fold"):
                    line = line.replace("fold along ", "")
                    l_type, coord = line.split("=")
                    folds.append((l_type, int(coord)))
                else:
                    x, y = line.strip().split(",")
                    points.add((int(x), int(y)))

        self._points = points
        self._folds = folds
    
    def solve(self):
        def y_mapping(x, y, num):
            return (x, num - (y - num)) if y > num else (x, y)

        def x_mapping(x, y, num):
            return (num - (x - num), y) if x > num else (x, y)

        for ind, (fold_type, coord) in enumerate(self._folds):
            if fold_type == "x":
                self._points = { x_mapping(*pt, coord) for pt in self._points }
            else:
                self._points = { y_mapping(*pt, coord) for pt in self._points }

            if ind == 0:
                print("p1: ", len(self._points))
    
    def print_points(self, x_range=10, y_range=20):
        for y in range(y_range):
            for x in range(x_range):
                if (x, y) in self._points:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

def solve(paper):
    paper.solve()
    paper.print_points(40, 10)

if __name__ == "__main__":
    solve(TransparentPaper())
