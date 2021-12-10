file = open("input05.txt").read().splitlines()

"""Input"""
coordinates = []
for i in range(len(file)):
    temp = file[i].strip().split(" -> ")
    temp[0] = temp[0].split(",")
    temp[0] = [int(x) for x in temp[0]]
    temp[1] = temp[1].split(",")
    temp[1] = [int(x) for x in temp[1]]
    temp[0].extend(temp[1])
    coordinates.append(temp[0])
# print(coordinates)

max = 0
for i in range(len(coordinates)):
    for j in range(4):
        if coordinates[i][j] > max:
            max = coordinates[i][j]
matrix = [[0 for i in range(max+1)] for i in range(max+1)]

"""Part One"""
for c in coordinates:
    if c[0] == c[2]:
        if c[1] <= c[3]:
            for i in range(c[1], c[3]+1):
                matrix[i][c[0]] += 1
        else:
            for i in range(c[1], c[3] - 1, -1):
                matrix[i][c[0]] += 1
    elif c[1] == c[3]:
        if c[0] <= c[2]:
            for i in range(c[0], c[2] + 1):
                matrix[c[1]][i] += 1
        else:
            for i in range(c[0], c[2] - 1, -1):
                matrix[c[1]][i] += 1

# for i in range(len(matrix)):
    # print(matrix[i])

counter = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] >= 2:
            counter += 1
print(counter)

"""Part Two"""
matrix = [[0 for i in range(max+1)] for i in range(max+1)]

for c in coordinates:
    if c[0] == c[2]:
        if c[1] <= c[3]:
            for i in range(c[1], c[3]+1):
                matrix[i][c[0]] += 1
        else:
            for i in range(c[1], c[3] - 1, -1):
                matrix[i][c[0]] += 1
    elif c[1] == c[3]:
        if c[0] <= c[2]:
            for i in range(c[0], c[2] + 1):
                matrix[c[1]][i] += 1
        else:
            for i in range(c[0], c[2] - 1, -1):
                matrix[c[1]][i] += 1
    else:
        x = c[0]
        y = c[1]
        if x < c[2] and y < c[3]:
            for i in range(c[2] + 1 - c[0]):
                matrix[y+i][x+i] += 1
        elif x < c[2] and y > c[3]:
            for i in range(c[2] + 1 - c[0]):
                matrix[y-i][x+i] += 1
        elif x > c[2] and y < c[3]:
            for i in range(c[0] + 1 - c[2]):
                matrix[y+i][x-i] += 1
        elif x > c[2] and y > c[3]:
            for i in range(c[0] + 1 - c[2]):
                matrix[y-i][x-i] += 1

# for i in range(len(matrix)):
    # print(matrix[i])

counter = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] >= 2:
            counter += 1
print(counter)
