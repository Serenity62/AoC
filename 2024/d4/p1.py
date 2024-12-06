#!/usr/bin/env python3

def parseInput(fn):
    grid = []
    with open(fn, "r") as f:
        ls = f.read().strip()
        for row in ls.split('\n'):
            grid.append([x for x in row])
    return grid


def checkR(grid, word):
    size = len(word)
    if size == 0:
        return 0
    rword = word[::-1]
    cnt = 0
    rng = int(len(grid) / size)
    for i in range(rng):
        for j in range(len(grid[i*size]) - size + 1):
            for k in range(size):
                row = ''.join(grid[i*size + k][j:j + size])
                if row in [word, rword]:
                    cnt += 1
    for i in range(len(grid) % size):
        for j in range(len(grid[i + rng * size]) - size + 1):
            row = ''.join(grid[i + rng * size][j: j + size])
            if row in [word, rword]:
                cnt += 1
    return cnt


def checkC(grid, word):
    size = len(word)
    if size == 0:
        return 0
    rword = word[::-1]
    cnt = 0
    for i in range(len(grid) - size + 1):
        rng = int(len(grid[i]) / size)
        for j in range(rng):
            for k in range(size):
                col = ''.join([x[k + j * size] for x in grid[i: i + size]])
                if col in [word, rword]:
                    cnt += 1
        for j in range(len(grid[i]) % size):
            col = ''.join([x[j + rng * size]
                          for x in grid[i: i + size]])
            if col in [word, rword]:
                cnt += 1
    return cnt


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
            if ldiag in [word, rword]:
                cnt += 1
            if rdiag in [word, rword]:
                cnt += 1
    return cnt


def main():
    # t = parseInput("test")
    t = parseInput("input")
    diag = findD(t, "XMAS")
    row = checkR(t, "XMAS")
    col = checkC(t, "XMAS")
    print(diag, row, col)
    print(diag + row + col)


if __name__ == "__main__":
    main()
