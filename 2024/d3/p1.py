#!/usr/bin/env python3
import re


def parseInput(fn):
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    prog = re.compile(pattern)
    with open(fn, "r") as f:
        ls = f.read().strip()
        muls = prog.findall(ls)
        return muls


def multiply(mul):
    a, b = mul
    return int(a) * int(b)


def main():
    # t = parseInput("test")
    t = parseInput("input")
    print(t)
    sum = 0
    for mul in t:
        sum += multiply(mul)
    print(sum)


if __name__ == "__main__":
    main()
