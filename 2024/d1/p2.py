#!/usr/bin/env python3

def parseInput(fn):
    with open(fn, "r") as f:
        ls = f.read().strip()
        left = []
        right = {}
        for l in ls.split('\n'):
            lft, rght = l.split('   ')
            left.append(int(lft))
            r = int(rght)
            if r in right:
                right[r] += 1
            else:
                right[r] = 1
        # left.sort()
        # print(right)
        return left, right


def compare(left, right):
    sum = 0
    for idx in left:
        diff = 0
        if idx in right:
            diff = idx * right[idx]
        # print(diff)
        sum += diff
    return sum


def main():
    # l, r = parseInput("test")
    l, r = parseInput("input")
    print(compare(l, r))


if __name__ == "__main__":
    main()
