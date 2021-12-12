import copy
from pprint import pprint

with open("input.txt") as f:
    arr = [line.strip().split("-") for line in f.readlines()]

#print(arr)

connections = {}

for line in arr:
    if line[0] in connections.keys():
        connections[line[0]].append(line[1])
    else:
        connections[line[0]] = [line[1]]

    if line[1] in connections.keys():
        connections[line[1]].append(line[0])
    else:
        connections[line[1]] = [line[0]]

#print(connections)

def find_paths(location, path, visited, dup):

    #print("Location: " + str(location) + " Paths: " + str(path) + " Visited: " + str(visited))
    new_path = copy.deepcopy(path)
    new_visited = copy.deepcopy(visited)

    if location == 'end':
        new_path.append('end')
        return [new_path]

    final_paths = []

    new_path.append(location)

    if location.islower():
        new_visited.append(location)

    for new_location in connections[location]:
        if new_location not in visited:
            final_paths += find_paths(new_location, new_path, new_visited, dup)
        elif new_location != 'start' and dup:
            final_paths += find_paths(new_location, new_path, new_visited, False)

    return final_paths


print(len(find_paths('start', [], [], False)))
print(len(find_paths('start', [], [], True)))
#pprint(find_paths_2('start', [], [], True))