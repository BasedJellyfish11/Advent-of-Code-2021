
with open("input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

feesh = arr[0].split(",")
feesh = [int(num) for num in feesh]

days = 256
max_age = 8

birth_rates = [ [None] * (max_age + 1) for i in range(days + 1)]

#print(feesh)
#print(birth_rates)

def final_feesh(fish_age, day):

    print("Age: " + str(fish_age) + " Day: " + str(day))

    if birth_rates[day][fish_age]:
        print("Job done - " + str(birth_rates[day][fish_age]))

        return birth_rates[day][fish_age]

    #print("Job not done")

    val = 0

    if (day + fish_age >= days):
        val = 1

    elif fish_age > 0:
        val = final_feesh(fish_age - 1, day + 1)

    else:
        val = final_feesh(6, day + 1) + final_feesh(8, day + 1)
        
    birth_rates[day][fish_age] = val

    return val
        

sum = 0

for num in feesh:
    sum += final_feesh(num, 0)

print(sum)