file = open("input9.txt").read().splitlines()

"""Part One"""
temp = []
for i in range(len(file)):
    for j in range(len(file[i])):
        bool = True
        if i-1 >= 0 and file[i-1][j] <= file[i][j]:
            bool = False
        if i+1 < len(file) and file[i+1][j] <= file[i][j]:
            bool = False
        if j-1 >= 0 and file[i][j-1] <= file[i][j]:
            bool = False
        if j+1 < len(file[0]) and file[i][j+1] <= file[i][j]:
            bool = False
        if bool:
            temp.append(file[i][j])
temp = [int(x) for x in temp]
# print(sum(temp)+len(temp))

"""Part Two"""
def size(file, marked, i, j):
    counter = 1
    marked[i][j] = True
    if file[i][j] == "9":
        return 0
    if i - 1 >= 0 and not marked[i - 1][j]:
        counter += size(file, marked, i-1, j)
    if i + 1 < len(file) and not marked[i + 1][j]:
        counter += size(file, marked, i+1, j)
    if j - 1 >= 0 and not marked[i][j-1]:
        counter += size(file, marked, i, j-1)
    if j + 1 < len(file[0]) and not marked[i][j+1]:
        counter += size(file, marked, i, j+1)
    return counter

temp = []
marked = [[False for i in range(len(file[0]))] for j in range(len(file))]

for i in range(len(file)):
    for j in range(len(file[i])):
        bool = True
        if i-1 >= 0 and file[i-1][j] <= file[i][j]:
            bool = False
        if i+1 < len(file) and file[i+1][j] <= file[i][j]:
            bool = False
        if j-1 >= 0 and file[i][j-1] <= file[i][j]:
            bool = False
        if j+1 < len(file[0]) and file[i][j+1] <= file[i][j]:
            bool = False
        if bool:
            temp.append(size(file, marked, i, j))
temp = sorted(temp)
print(temp[-1]*temp[-2]*temp[-3])
