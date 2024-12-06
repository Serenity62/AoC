#!/usr/bin/python3

def parseInput(fn):
    f = open(fn, "r")

    t = int(f.readline().split(":")[1].replace(" ", ""))
    d = int(f.readline().split(":")[1].replace(" ", ""))
    f.close()
    return (t, d)

def race(t, hold):
    return (t - hold) * hold

def ways(time, best):
    low = 0
    high = 0

    for t in range(1, time-1):
        if race(time, t) > best:
            low = t
            break
    for t in range(1, time-1)[::-1]:
        if race(time, t) > best:
            high = t
            break

    return high - low + 1

def main():
    (times, dists)  = parseInput("input")
    print(times)
    print(dists)
    r = ways(times, dists)
    print(r)

if __name__ == "__main__":
    main()
