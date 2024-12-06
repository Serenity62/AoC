#!/usr/bin/python3

def parseInput(fn):
    f = open(fn, "r")

    t = f.readline().split(":")[1].split(" ")
    times = []
    for time in t:
        if time != "":
            times.append(int(time))

    d = f.readline().split(":")[1].split(" ")
    dists = []
    for dist in d:
        if dist != "":
            dists.append(int(dist))

    f.close()
    return (times, dists)

def race(t, hold):
    return (t - hold) * hold

def ways(time, best):
    p = 0

    for t in range(1, time-1):
        if race(time, t) > best:
            p += 1

    return p

def main():
    (times, dists)  = parseInput("input")
    print(times)
    print(dists)
    races = []
    total = 1
    for i in range(len(times)):
        r = ways(times[i], dists[i])
        races.append(r)
        total *= r
    print(races)
    print(total)

if __name__ == "__main__":
    main()
