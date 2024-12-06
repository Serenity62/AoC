#!/usr/bin/python3

def parseInput(fn):
    f = open(fn, "r")

    maps = [ "s2s", "s2f", "f2w", "w2l", "l2t", "t2h", "h2l" ]
    almanac = {"maps": maps}

    a = f.read()[:-1].split("\n\n")
    #print(a)
    # Seeds
    ss = []
    seeds = a[0].split(": ")[1].split(" ")
    for i in range(0, len(seeds), 2):
        for j in range(int(seeds[i+1])-1):
            ss.append(int(seeds[i]) + j)
    almanac["seeds"] = ss
    
    for i, m in enumerate(maps):
        ts = a[i+1].split("\n")[1:]
        #print(ts)
        src = []
        dst = []
        rge = []
        for t in ts:
            #almanac[m].append(t.split(" "))
            if t != "":
                t = t.split(" ")
                #for j in range(int(t[2])):
                #   src.append(int(t[1])+j)
                #   dst.append(int(t[0])+j)
                src.append(int(t[1]))
                dst.append(int(t[0]))
                rge.append(int(t[2]))
        almanac[m] = [src, dst, rge]

    f.close()
    return almanac

def map(a):
    loc = {}
    for s in a["seeds"]:
        t = int(s)
        for m in a["maps"]:
            for i in range(len(a[m][0])):
                if t >= a[m][0][i] and t <= a[m][0][i] + a[m][2][i] - 1:
                    d = t - a[m][0][i]
                    t = a[m][1][i] + d
                    break
        loc[s] = t
    return loc

def main():
    almanac = parseInput("input")
    #print(almanac)
    loc = map(almanac)
    print(loc)

    min = -1
    for l in loc.values():
        if min == -1 or min > l:
            min = l
    print(min)

if __name__ == "__main__":
    main()
