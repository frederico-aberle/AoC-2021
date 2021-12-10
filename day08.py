file = open("input08.txt").readlines()

"""Part One"""
result = 0
for x in file:
    temp = x.strip().split("|")
    digits = temp[0].split()
    four = temp[1].split()
    # print(digits)
    # print(four)

    for x in four:
        if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
            result += 1
print(result)

"""Part Two"""
result = 0
d = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}
for x in file:
    temp = x.strip().split("|")
    digits = temp[0].split()
    output = temp[1].split()
    # print(digits)
    # print(four)
    for y in digits:
        if len(y) == 2: # digit 1
            one = y
        elif len(y) == 4: # digit 4
            four = y
        elif len(y) == 3: # digit 7
            seven = y
        elif len(y) == 7: # digit 8
            eight = y
    # fill a
    for y in seven:
        if y not in one:
            d["a"] = y
    # fill c and f
    counter = 0
    for y in digits:
        if one[0] in y:
            counter += 1
    if counter == 8:
        d["c"] = one[0]
        d["f"] = one[1]
    else:
        d["c"] = one[1]
        d["f"] = one[0]
    # fill b and d
    left = ""
    for y in four:
        if y != d["a"] and y != d["c"] and y != d["f"]:
            left += y
    counter = 0
    for y in digits:
        if left[0] in y:
            counter += 1
    if counter == 6:
        d["b"] = left[0]
        d["d"] = left[1]
    else:
        d["b"] = left[1]
        d["d"] = left[0]
    # fill e and g
    left = ""
    for y in eight:
        if y not in four and y not in seven:
            left += y
    counter = 0
    for y in digits:
        if left[0] in y:
            counter += 1
    if counter == 4:
        d["e"] = left[0]
        d["g"] = left[1]
    else:
        d["e"] = left[1]
        d["g"] = left[0]

    zero = d["a"] + d["b"] + d["c"] + d["e"] + d["f"] + d["g"]
    one = d["c"] + d["f"]
    two = d["a"] + d["c"] + d["d"] + d["e"] + d["g"]
    three = d["a"] + d["c"] + d["d"] + d["f"] + d["g"]
    four = d["b"] + d["c"] + d["d"] + d["f"]
    five = d["a"] + d["b"] + d["d"] + d["f"] + d["g"]
    six = d["a"] + d["b"] + d["d"] + d["e"] + d["f"] + d["g"]
    seven = d["a"] + d["c"] + d["f"]
    eight = d["a"] + d["b"] + d["c"] + d["d"] + d["e"] + d["f"] + d["g"]
    nine = d["a"] + d["b"] + d["d"] + d["e"] + d["f"]

    number = ""
    for y in output:
        if sorted(y) == sorted(zero):
            number += "0"
        elif sorted(y) == sorted(one):
            number += "1"
        elif sorted(y) == sorted(two):
            number += "2"
        elif sorted(y) == sorted(three):
            number += "3"
        elif sorted(y) == sorted(four):
            number += "4"
        elif sorted(y) == sorted(five):
            number += "5"
        elif sorted(y) == sorted(six):
            number += "6"
        elif sorted(y) == sorted(seven):
            number += "7"
        elif sorted(y) == sorted(eight):
            number += "8"
        else:
            number += "9"

    result += int(number)

print(result)
