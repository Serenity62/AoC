#!/usr/bin/env python3

def parseInput(fn):
    with open(fn, "r") as f:
        ls = f.read().strip()
        return ls


def genDisk(dmap):
    file = True
    id = 0
    disk = []
    for idx in range(len(dmap)):
        for _ in range(int(dmap[idx])):
            disk.append(str(id) if file else '.')
        file = not file
        if file:
            id += 1
    return disk


def moveBlocks(disk):
    lidx = len(disk) - 1
    for idx in range(len(disk)):
        if disk[idx] == '.':
            while True:
                if lidx < 0:
                    return disk
                elif lidx <= idx:
                    return disk
                elif disk[lidx].isdigit():
                    disk[idx] = disk[lidx]
                    disk[lidx] = '.'
                    lidx -= 1
                    break
                lidx -= 1
    return disk


def checkSum(disk):
    sum = 0
    for idx in range(len(disk)):
        char = disk[idx]
        if char != '.':
            sum += idx * int(char)
    return sum


def main():
    # t = parseInput("test")
    # t = parseInput("test2")
    t = parseInput("input")

    disk = genDisk(t)
    moved = moveBlocks(disk)
    print(checkSum(moved))


if __name__ == "__main__":
    main()
