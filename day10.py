file = open("input10.txt").read().splitlines()

open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]
value = [3, 57, 1197, 25137]

result = 0
for s in file:
    stack = []
    for i in range(len(s)):
        if s[i] in open:
            stack.append(s[i])
        elif s[i] in close:
            if stack[-1] == open[close.index(s[i])]:
                stack = stack[:-1]
            else:
                result += value[close.index(s[i])]
                break
print(result)

"""Part Two"""
open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]

result = []

for s in file:
    stack = []
    bool = True
    for i in range(len(s)):
        if s[i] in open:
            stack.append(s[i])
        elif s[i] in close:
            if stack[-1] == open[close.index(s[i])]:
                stack = stack[:-1]
            else:
                bool = False
                break
    if bool:
        temp = 0
        for i in range(len(stack) - 1, -1, -1):
            temp *= 5
            temp += open.index(stack[i]) + 1
        result.append(temp)

result = sorted(result)

print(result[len(result)//2])
