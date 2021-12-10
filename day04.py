file = open("input04.txt")

"""Input"""
numbers = file.readline().split(",")
numbers = [int(x) for x in numbers]

file = file.read().splitlines()

for i in range(len(file)):
    file[i] = file[i].split(" ")

bingos = []
i = 0
while i < len(file):
    if file[i] == ['']:
        i += 1
    else:
        oneBingo = []
        for j in range(5):
            temp = []
            for k in range(len(file[i])):
                if file[i][k] != '':
                    temp.append(int(file[i][k]))
            oneBingo.append(temp)
            i += 1
        bingos.append(oneBingo)
# print(bingos)

def isBingo(marked):
    # horizontal
    for i in range(5):
        if marked[i] == [True for j in range(5)]:
            return True

    # vertical
    for j in range(5):
        bool1 = True
        for i in range(5):
            if not marked[i][j]:
                bool1 = False
        if bool1:
            return True

"""Part One"""

index = len(numbers)
for i in range(len(bingos)):
    bingo = bingos[i]
    marked = [[False for i in range(5)] for j in range(5)]

    j = 0
    while j != len(numbers):
        for a in range(5):
            for b in range(5):
                if bingo[a][b] == numbers[j]:
                    marked[a][b] = True
                    break
        if isBingo(marked):
            # print(marked)
            break
        j += 1

    if j < index:
        index = j
        sum = 0
        for a in range(5):
            for b in range(5):
                if not marked[a][b]:
                    sum += bingo[a][b]

print(sum * numbers[index])

"""Part Two"""

index = 0
for i in range(len(bingos)):
    bingo = bingos[i]
    marked = [[False for i in range(5)] for j in range(5)]

    j = 0
    while j != len(numbers):
        for a in range(5):
            for b in range(5):
                if bingo[a][b] == numbers[j]:
                    marked[a][b] = True
                    break
        if isBingo(marked):
            # print(marked)
            break
        j += 1

    if j > index:
        index = j
        sum = 0
        for a in range(5):
            for b in range(5):
                if not marked[a][b]:
                    sum += bingo[a][b]

print(sum * numbers[index])



