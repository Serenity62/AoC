#!/usr/bin/env python3

def parseInput(fn):
    with open(fn, "r") as f:
        ls = f.read().strip()
        return ls


def genDisk(dmap):
    file = True
    id = 0
    disk = []
    empty = []
    files = []
    for idx in range(len(dmap)):
        tmp = int(dmap[idx])
        for _ in range(tmp):
            disk.append(str(id) if file else '.')
        if file:
            if id > 0:
                # File ID, index, size
                files.append((id, len(disk) - tmp, tmp))
            id += 1
        else:
            empty.append((len(disk) - tmp, tmp))  # index, size
        file = not file
    return disk, empty, files


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


def moveBlocks2(disk, empty, files):
    # Investigate about recalulating empty list.
    if len(files) == 0 or len(empty) == 0:
        return disk
    for idx in range(len(files) - 1, -1, -1):
        fid, index, size = files[idx]
        for edx in range(len(empty)):
            est, esize = empty[edx]
            if est >= index:
                return disk
            elif esize >= size:
                for i in range(size):
                    disk[est+i] = str(fid)
                    disk[index+i] = '.'
                files.pop()
                if esize == size:
                    empty.pop(edx)
                else:
                    empty[edx] = (est + size, esize - size)
                print(''.join(disk))
                break
    return moveBlocks2(disk, empty, files)


def checkSum(disk):
    sum = 0
    for idx in range(len(disk)):
        char = disk[idx]
        if char != '.':
            sum += idx * int(char)
    return sum


def main():
    # t = parseInput("test")
    t = parseInput("test2")
    # t = parseInput("input")

    disk, empty, files = genDisk(t)
    print(empty)
    print(files)
    print(''.join(disk))
    moved = moveBlocks2(disk, empty, files)
    print(checkSum(moved))


if __name__ == "__main__":
    main()
