#!/usr/bin/python3
def getdigit(s):
    v = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    first = -1
    last = -1
    fd = 0
    ld = 0
    for idx, i in enumerate(v):
        try:
            j = s.index(i)
            if first == -1 or first > j:
                first = j
                fd = (idx % 9) + 1
        except:
            pass
        try:
            j = s.rindex(i)
            if last == -1 or last < j:
                last = j
                ld = (idx % 9) + 1
        except:
            pass
    return (fd, ld)


f = open("input1", "r")

input_list = []
s = 0

for i in f:
    #input_list.append(i.strip("\n"))
    x, y = getdigit(i)
    z = (x * 10) + y
    s += z
    input_list.append(z)

f.close()
print(input_list)
print(s)



