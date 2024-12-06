#!/usr/bin/python3

_invDir = { "n": "s",
          "s": "n",
          "e": "w",
          "w": "e" }

def parseInput(fn):
    f = open(fn, "r")
    ls = f.read().strip().split("\n")
    map = []
    start = None

    for l in ls:
        r = []
        for c in range(len(l)):
            r.append(l[c])
            if l[c] == "S":
                start = [len(map), c]
        map.append(r)

    f.close()
    return (map, start)

def pipeEnd(p, s):
    match p:
        case '|':
            return "n" if s == "s" else "s"
        case '-':
            return "e" if s == "w" else "w"
        case 'L':
            return "n" if s == "e" else "e"
        case 'J':
            return "n" if s == "w" else "w"
        case '7':
            return "s" if s == "w" else "w"
        case 'F':
            return "s" if s == "e" else "e"
        case _:
            raise Exception("Case out of bounds")

def getPath(m, s):
    path = [["." for i in range(len(m[0]))] for i in range(len(m))]
    flag = True
    p1 = s
    p2 = s
    i = 0
    while flag:
        if i == 0:
            pflag = False
            x = p1[0]
            y = p1[1]
            path[x][y] = "S"
            try:
                pipe = m[x-1][y]
                if pipe in ["|", "7", "F"]:
                    pflag = True
                    p1[0] = x-1
                    p1.append("s")
                    p1.append(pipe)
            except:
                pass
            try:
                pipe = m[x][y+1]
                if pipe in ["-", "J", "7"]:
                    tmp = [x, y+1, "w", pipe]
                    if pflag:
                        p2 = tmp
                    else:
                        pflag = True
                        p1 = tmp
            except:
                pass
            try:
                pipe = m[x+1][y]
                if pipe in ["|", "L", "J"]:
                    tmp = [x+1, y, "n", pipe]
                    if pflag:
                        p2 = tmp
                    else:
                        pflag = True
                        p1 = tmp
            except:
                pass
            try:
                pipe = m[x][y-1]
                if pipe in ["-", "L", "F"]:
                    p2[1] = y-1
                    p2.append("e")
                    p2.append(pipe)
            except:
                pass
            #print((p1, p2))
        else:
            dir1 = pipeEnd(p1[3], p1[2])
            dir2 = pipeEnd(p2[3], p2[2])
            tps = []
            for d in [dir1, dir2]:
                x = 0
                y = 0
                match d:
                    case "n":
                        x = -1
                    case "e":
                        y = 1
                    case "s":
                        x = 1
                    case "w":
                        y = -1
                tps.append([x, y])
            p1[0] += tps[0][0]
            p1[1] += tps[0][1]
            p1[3] = m[p1[0]][p1[1]]
            p1[2] = _invDir[dir1]
            p2[0] += tps[1][0]
            p2[1] += tps[1][1]
            p2[3] = m[p2[0]][p2[1]]
            p2[2] = _invDir[dir2]

        i += 1
        if path[p1[0]][p1[1]] == ".":
            path[p1[0]][p1[1]] = p1[3]
        else:
            flag = False
        if path[p2[0]][p2[1]] == ".":
            path[p2[0]][p2[1]] = p2[3]
        else:
            flag = False
    print((p1, p2))
    return (path, i)

def findInner(m):
    inner = 0

    for x in range(len(m)):
        end = [0, len(m[0])-1]
        if x == 0 or x == len(m)-1:
            end = range(0, len(m[0]))
        for y in end:
            #print((x, y))
            if m[x][y] == ".":
                m[x][y] = "O"
    return (m, inner)

def printMap(m):
    for r in m:
        t = ''.join(r)
        print(t)

def main():
    m, s = parseInput("p2test")
    printMap(m)
    print()
    p, i = getPath(m, s)
    printMap(p)
    print(i)
    print()
    mm, inner = findInner(m)
    printMap(mm)
    print(inner)

if __name__ == "__main__":
    main()
