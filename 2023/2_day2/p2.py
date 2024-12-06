#!/usr/bin/python3

def parseRound(r):
    #print(r)
    pr = { "red": 0, "green": 0, "blue": 0 }
    for i in r.split(","):
        c = i.strip(" ").split(" ")
        pr[c[1]] = int(c[0])
    #print(pr)
    return pr

def parseInput():
    f = open("input", "r")
    games = []
    for i in f:
        game = {}
        game["id"] = int(i[i.index(" "):i.index(":"):])
        rs = i[i.index(":")+1:].replace("\n", "").split(";")
        ra = []
        for r in rs:
            ra.append(parseRound(r))
        game["rounds"] = ra
        games.append(game)
    return games

def possible(rs, config):
    low = {}
    possible = True
    for r in rs:
        for key, val in r.items():
            if val > config[key]:
                possible = False
            try:
                if low[key] < val:
                    low[key] = val
            except:
                low[key] = val
    return (possible, low)

def power(r):
    x = 1
    for c, v in r.items():
        if v != 0:
            x = x * v
    return x    

def main():
    val = { "red": 12,
           "green": 13,
           "blue": 14}
    games = parseInput()
    s = 0
    for g in games:
        p, low = possible(g["rounds"], val)
        s += power(low)
    print(s)
    #print(games)

if __name__ == "__main__":
    main()
