file = open("input1.txt").read().splitlines()
file = [int(x) for x in file]

"""Part One"""
counter = 0
for i in range(1, len(file)):
    if file[i] - file[i-1] > 0:
        counter += 1
print(counter)

"""Part Two"""
temp = []
for i in range(len(file)-2):
    temp.append(sum(file[i:i+3]))
counter = 0
for i in range(1, len(temp)):
    if temp[i] - temp[i-1] > 0:
        counter += 1
print(counter)
