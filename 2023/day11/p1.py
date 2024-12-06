#!/usr/bin/python3

def parseInput(fn):
    col = []
    map = []
    pos = {}
    cnt = 1
    f = open(fn, "r")
    ls = f.read().strip().split("\n")
    for line in ls:
        empty = True
        r = []
        for i in range(len(line)):
            if len(col) < len(line):
                col.append(True)
            c = line[i]
            if c != ".":
                empty = False
                col[i] = False
            r.append(c)
        map.append(r)
        if empty:
            map.append(r)
    printMap(map)
    tmp = 0
    for j, c in enumerate(col):
        if c:
            for i in range(len(map)):
                map[i].insert(j+tmp, ".")
            tmp += 1
    for i in range(len(map)):
        for j in range(len(map[i])):
            c = map[i][j]
            if c == "#":
                map[i][j] = str(cnt)
                pos[cnt] = [i, j]
                cnt += 1
    f.close()
    return (map, pos)

def printMap(m):
    for r in m:
        print(''.join(r))

def main():
    m, p = parseInput("test")
    printMap(m)
    print(p)

if __name__ == "__main__":
    main()
