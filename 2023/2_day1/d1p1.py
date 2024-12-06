#!/usr/bin/python3
def firstdigit(s):
    for i in s:
        if i.isdigit():
            return int(i)
    return 0


f = open("input1", "r")

input_list = []
s = 0

for i in f:
    #input_list.append(i.strip("\n"))
    x = 10 * firstdigit(i)
    x += firstdigit(i[::-1])
    s += x

f.close()

print(s)



