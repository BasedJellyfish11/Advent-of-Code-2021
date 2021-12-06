text_file = open("input.txt", "r")
arr = text_file.read().split('\n')

tot = 0

for i in range(1, len(arr)):
    if int(arr[i]) > int(arr[i-1]):
        tot += 1

print(tot)

tot = 0

for i in range(len(arr) - 2):
    if int(arr[i + 3]) > int(arr[i]):
        tot += 1
    #print(tot)

print(tot)