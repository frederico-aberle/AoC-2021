file = open("input07.txt").read().split(",")
temp = sorted([int(x) for x in file])

"""Part One"""
result = float("inf")
for pos in range(temp[0], temp[-1]+1):
    counter = 0
    for j in range(len(temp)):
        counter += abs(pos-temp[j])
    if counter < result:
        result = counter
    else:
        break

# print(result)

"""Part Two"""
result = float("inf")

for pos in range(temp[0], temp[-1]+1):
    counter = 0
    for j in range(len(temp)):
        counter += (abs(pos-temp[j])*(abs(pos-temp[j])+1))/2
    if counter < result:
        result = counter
    else:
        break

print(int(result))
