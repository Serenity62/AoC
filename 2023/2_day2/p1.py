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
    for r in rs:
        for key, val in r.items():
            if val > config[key]:
                return False
    return True

def main():
    val = { "red": 12,
           "green": 13,
           "blue": 14}
    games = parseInput()
    s = 0
    for g in games:
        if possible(g["rounds"], val):
            s += g["id"]
    print(s)
    #print(games)

if __name__ == "__main__":
    main()
