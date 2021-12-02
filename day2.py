file = open("input2.txt").read().splitlines()

horizontal = 0
depth = 0
aim = 0
for i in range(len(file)):
    temp = file[i].split()
    if temp[0] == 'forward':
        horizontal += int(temp[1])
        depth += aim * int(temp[1])
    elif temp[0] == 'up':
        aim -= int(temp[1])
    elif temp[0] == 'down':
        aim += int(temp[1])

print(horizontal*depth)
