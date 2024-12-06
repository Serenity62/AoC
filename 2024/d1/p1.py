#!/usr/bin/env python3

def parseInput(fn):
    with open(fn, "r") as f:
        ls = f.read().strip()
        left = []
        right = []
        for l in ls.split('\n'):
            lft, rght = l.split('   ')
            left.append(int(lft))
            right.append(int(rght))
        left.sort()
        right.sort()
        return left, right


def compare(left, right):
    sum = 0
    for idx in range(len(left)):
        diff = abs(left[idx] - right[idx])
        # print(diff)
        sum += diff
    return sum


def main():
    # l, r = parseInput("test")
    l, r = parseInput("input")
    print(compare(l, r))


if __name__ == "__main__":
    main()
