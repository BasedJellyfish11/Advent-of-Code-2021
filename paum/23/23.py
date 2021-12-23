import copy
import time

hall_len = 11

letter_room_positions = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
letter_rooms = {'A': (11, 12, 13, 14), 'B': (15, 16, 17, 18), 'C': (19, 20, 21, 22), 'D': (23, 24, 25, 26)}
idx_room_positions = {11: 2, 12: 2, 13: 2, 14: 2, 15: 4, 16: 4, 17: 4, 18: 4, 19: 6, 20: 6, 21: 6, 22: 6, 23: 8, 24: 8, 25: 8, 26: 8}
letter_energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
goal_hall = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D']

def is_comfy(hall, idx, char):
    if idx not in letter_rooms[char]:
        return False
    
    for i in range(idx + 1, 30):
        if (i + 1) % 4 == 0:
            return True
        if hall[i] != char:
            return False

def deepness(idx):
    return ((idx + 1) % 4) + 1

def find_valid_resting(hall, char):
    resting_options = letter_rooms[char]
    for option in reversed(resting_options):
        if hall[option] == '.':
            return option
        if hall[option] != char:
            return False

    print("ERROR VALID")

def stuckness(i):
    return 10 - abs(i - 5)

def is_stuck(hall, idx):
    for i in range(idx - 1, 0, -1):
        if (i + 2) % 4 == 0:
            return False
        if hall[i] != '.':
            return True
        
    print("ERROR STUCK")

def find_legal_moves(hall, idx, char):

    #Starting in Hall
    if idx < hall_len:

        final_idx = find_valid_resting(hall, char)
        if not final_idx:
            return []

        room_location = letter_room_positions[char]
        path = hall[idx + 1 : room_location + 1] if idx < room_location else hall[room_location : idx]
        if path.count('.') != len(path):
            return []

        return [((idx, final_idx), len(path) + deepness(final_idx), 0)]
    
    #Starting in Room
    if is_comfy(hall, idx, char):
        return []

    if is_stuck(hall, idx):
        return []

    moves = []
    end_path = idx_room_positions[idx]
    energy = deepness(idx) - 1

    for i in range(end_path, -1, -1):
        energy += 1
        if i in letter_room_positions.values():
            continue
        val = hall[i]
        if val != '.':
            break
        moves.append(((idx, i), energy, stuckness(i) + energy))
    
    energy = deepness(idx) - 1

    for i in range(end_path, 11):
        energy += 1
        if i in letter_room_positions.values():
            continue
        val = hall[i]
        if val != '.':
            break
        moves.append(((idx, i), energy, stuckness(i) + energy))

    return moves

def find_moves(hall):

    char_movements = []

    for idx, char in enumerate(hall):
        if char != '.':
            char_movements += find_legal_moves(hall, idx, char)
    
    if len(char_movements) > 0:
        char_movements.sort(key = lambda x:(x[2], x[1]))

    return char_movements
        
def make_move(hall, move):

    a, b = move
    hall[a], hall[b] = hall[b], hall[a]

def solve(hall, energy, max_energy):

    cur_best = max_energy
    moves = find_moves(hall)

    if not len(moves) and hall == goal_hall:
        return energy

    for move in moves:

        #print(move)
        new_energy = energy + (move[1] * letter_energy[hall[move[0][0]]])

        if new_energy < cur_best:
            new_hall = copy.deepcopy(hall)
            make_move(new_hall, move[0])
            #print(f"Hall: \n{new_hall}")
            #print(f"Move: {move[0]}")
            #print(f"Energy: {new_energy}\n")
            #time.sleep(0.1)
            cur_best = solve(new_hall, new_energy, cur_best)
    
    if cur_best < max_energy:
        print(f"New Best: {cur_best}", flush=True)


    return cur_best

def main():

    #test_hallway = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D']
    hallway = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', 'D', 'D', 'B', 'D', 'C', 'B', 'C', 'A', 'B', 'A', 'D', 'B', 'A', 'C', 'C']
    test_hallway = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', 'D', 'D', 'A', 'C', 'C', 'B', 'D', 'B', 'B', 'A', 'C', 'D', 'A', 'C', 'A']
    print(solve(hallway, 0, 400000))

if __name__ == "__main__":
    #print(['1', '2', '3'] == ['1', '2', '3'])
    main()