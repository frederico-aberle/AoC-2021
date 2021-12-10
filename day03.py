file = open("input03.txt").read().splitlines()

"""Part One"""
gamma = ""
epsilon = ""
for j in range(len(file[0])):
    counter = 0
    for i in range(len(file)):
        if file[i][j] == "0":
            counter += 1
    if counter >= len(file)-counter:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

def binToDec(bin):
    dec = 0
    exp = 0
    for i in range(len(bin)-1, -1, -1):
        if int(bin[i]) == 1:
            dec += 2 ** exp
        exp += 1
    return dec
print(binToDec(gamma) * binToDec(epsilon))

"""Part Two"""
oxygen = file
for j in range(len(oxygen[0])):
    counter = 0
    for i in range(len(oxygen)):
        if oxygen[i][j] == "0":
            counter += 1
    if counter > len(oxygen)-counter:
        temp = []
        for i in range(len(oxygen)):
            if oxygen[i][j] == "0":
                temp.append(oxygen[i])
        oxygen = temp
    else:
        temp = []
        for i in range(len(oxygen)):
            if oxygen[i][j] == "1":
                temp.append(oxygen[i])
        oxygen = temp
    if len(oxygen) == 1:
        break

carbondioxide = file
for j in range(len(carbondioxide[0])):
    counter = 0
    for i in range(len(carbondioxide)):
        if carbondioxide[i][j] == "0":
            counter += 1
    if counter <= len(carbondioxide)-counter:
        temp = []
        for i in range(len(carbondioxide)):
            if carbondioxide[i][j] == "0":
                temp.append(carbondioxide[i])
        carbondioxide = temp
    else:
        temp = []
        for i in range(len(carbondioxide)):
            if carbondioxide[i][j] == "1":
                temp.append(carbondioxide[i])
        carbondioxide = temp
    if len(carbondioxide) == 1:
        break
print(binToDec(oxygen[0]) * binToDec(carbondioxide[0]))


