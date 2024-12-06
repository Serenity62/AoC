#!/usr/bin/python3

def parseInput(fn):
    f = open(fn, "r")
    ls = f.read().strip().split("\n")

    hist = []
    fut = []
    tt = []
    for l in ls:
        t = l.split(" ")
        t = list(map(int, t))
        hist.append(t)
        fut.append(future(t) + t[-1])
        x = t[::-1]
        tt.append(future(x) + x[-1])

    f.close()
    return (hist, fut, tt)

def future(h):
    zero = True
    dif = []
    for i in range(1,len(h)):
        t = h[i] - h[i-1]
        dif.append(t)
        if t != 0:
            zero = False
    if not zero:
        n = future(dif)
        return dif[-1] + n
    return 0

def main():
    history, futures, tt = parseInput("input")
    print(history, futures, tt)
    print(sum(futures))
    print(sum(tt))
    
if __name__ == "__main__":
    main()
