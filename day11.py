file = open("input11.txt").read().splitlines()

"""Part One"""
grid = file
temp = []
for x in grid:
    line = []
    for i in range(len(x)):
        line.append(int(x[i]))
    temp.append(line)
grid = temp

def count(temp, i, j, increases):
    if i-1 >= 0 and j-1 >= 0:
        increases[i-1][j-1] += 1
    if i-1 >= 0:
        increases[i-1][j] += 1
    if i-1 >= 0 and j+1 < len(temp):
        increases[i-1][j+1] += 1
    if j-1 >= 0:
        increases[i][j-1] += 1
    if j+1 < len(temp):
        increases[i][j+1] += 1
    if i+1 < len(temp) and j-1 >= 0:
        increases[i+1][j-1] += 1
    if i+1 < len(temp):
        increases[i+1][j] += 1
    if i+1 < len(temp) and j+1 < len(temp):
        increases[i+1][j+1] += 1
    return increases

temp = []
for i in range(len(grid)):
    temp.append(grid[i].copy())

result = 0
for steps in range(100):

    for i in range(len(grid)):
        for j in range(len(grid)):
            temp[i][j] += 1

    flashed = [[False for x in range(len(grid))] for y in range(len(grid))]

    while True:

        increases = [[0 for x in range(len(grid))] for y in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid)):
                if temp[i][j] > 9 and not flashed[i][j]:
                    increases = count(temp, i , j, increases)
                    flashed[i][j] = True

        for i in range(len(grid)):
            for j in range(len(grid)):
                temp[i][j] += increases[i][j]

        if increases == [[0 for x in range(len(grid))] for y in range(len(grid))]:
            break

    for i in range(len(grid)):
        for j in range(len(grid)):
            if temp[i][j] > 9:
                temp[i][j] = 0

    for i in range(len(flashed)):
        result += flashed[i].count(True)

print(result)

"""Part Two"""
temp = []
for i in range(len(grid)):
    temp.append(grid[i].copy())

step = 1
while True:

    for i in range(len(grid)):
        for j in range(len(grid)):
            temp[i][j] += 1

    flashed = [[False for x in range(len(grid))] for y in range(len(grid))]

    while True:

        increases = [[0 for x in range(len(grid))] for y in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid)):
                if temp[i][j] > 9 and not flashed[i][j]:
                    increases = count(temp, i , j, increases)
                    flashed[i][j] = True

        for i in range(len(grid)):
            for j in range(len(grid)):
                temp[i][j] += increases[i][j]

        if increases == [[0 for x in range(len(grid))] for y in range(len(grid))]:
            break

    for i in range(len(grid)):
        for j in range(len(grid)):
            if temp[i][j] > 9:
                temp[i][j] = 0

    if flashed == [[True for x in range(len(grid))] for y in range(len(grid))]:
        print(step)
        break

    step += 1
