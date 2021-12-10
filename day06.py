file = open("input06.txt").readline().split(',')
file = [int(x) for x in file]

"""Part One"""
temp = file
for i in range(18):
    for j in range(len(temp)):
        if temp[j] == 0:
            temp[j] = 6
            temp.append(8)
        else:
            temp[j] -= 1
    # print(temp)
print(len(temp))

"""Part Two"""
temp = file
days = [0] * 9

for x in temp:
    days[x] += 1

for i in range(256):
    today = i % len(days)
    days[(today + 7) % len(days)] += days[today]
print(sum(days))
