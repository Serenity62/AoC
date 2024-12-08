#!/usr/bin/env python3

def parseInput(fn):
    nodes = {}
    grid = []
    with open(fn, "r") as f:
        ls = f.read().strip()
        rows = ls.split('\n')
        for i in range(len(rows)):
            row = [x for x in rows[i]]
            grid.append(['.' for x in range(len(row))])
            for j in range(len(row)):
                char = row[j]
                if char != '.':
                    if char not in nodes:
                        nodes[char] = []
                    nodes[char].append((i, j))
    return nodes, grid


def printGrid(grid):
    for row in grid:
        print(''.join(row))


def addANode(i, j, grid):
    try:
        if grid[i][j] == '#' or i < 0 or j < 0:
            return False, grid
        grid[i][j] = '#'
        return True, grid
    except IndexError:
        return False, grid


def findANodes(feqArr, grid):
    sum = 0
    if len(feqArr) <= 1:
        return grid, 0
    i, j = feqArr[0]
    tmp = feqArr[1:]
    for feq in tmp:
        k, l = feq
        di = k - i
        dj = l - j
        ti, tj = i, j
        while True:
            res, grid = addANode(ti, tj, grid)
            if res:
                sum += 1
            ti = ti - di
            tj = tj - dj
            if ti < 0 or tj < 0 or tj >= len(grid[0]):
                break
        ti, tj = k, l
        while True:
            res, grid = addANode(ti, tj, grid)
            if res:
                sum += 1
            ti = ti + di
            tj = tj + dj
            if ti >= len(grid) or tj < 0 or tj >= len(grid[0]):
                break
    ngrid, anodes = findANodes(tmp, grid)
    sum += anodes
    return ngrid, sum


def main():
    # nodes, grid = parseInput("test")
    # nodes, grid = parseInput("test2")
    nodes, grid = parseInput("input")
    print(nodes)
    total = 0
    for k, v in nodes.items():
        if k == '#':
            continue
        grid, sum = findANodes(v, grid)
        total += sum
    printGrid(grid)
    print(total)


if __name__ == "__main__":
    main()
