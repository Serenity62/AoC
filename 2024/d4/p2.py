#!/usr/bin/env python3

def parseInput(fn):
    grid = []
    with open(fn, "r") as f:
        ls = f.read().strip()
        for row in ls.split('\n'):
            grid.append([x for x in row])
    return grid


def findD(grid, word):
    size = len(word)
    rword = word[::-1]
    cnt = 0
    for i in range(len(grid)-size + 1):
        for j in range(len(grid[i]) - size + 1):
            ldiag = ""
            rdiag = ""
            for k in range(size):
                ldiag += grid[i + k][j + k]
                rdiag += grid[i + k][j + size - 1 - k]
            if ldiag in [word, rword] and rdiag in [word, rword]:
                cnt += 1
    return cnt


def main():
    # t = parseInput("test")
    t = parseInput("input")
    diag = findD(t, "MAS")
    print(diag)


if __name__ == "__main__":
    main()
