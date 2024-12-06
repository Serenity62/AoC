#!/usr/bin/env python3
import re


def todos(input):
    split = input.split("don't()")
    dos = [split[0]]
    if len(split) > 1:
        split = split[1:]
        for p in split:
            do = p.split("do()")
            if len(do) > 1:
                dos.append(''.join(do[1:]))
    return dos


def parseInput(fn):
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    prog = re.compile(pattern)
    muls = []
    with open(fn, "r") as f:
        ls = f.read().strip()
        dos = todos(ls)
        print(dos)
        for do in dos:
            muls.extend(prog.findall(do))
        return muls


def multiply(mul):
    a, b = mul
    return int(a) * int(b)


def main():
    # t = parseInput("test2")
    t = parseInput("input")
    print(t)
    sum = 0
    for mul in t:
        sum += multiply(mul)
    print(sum)


if __name__ == "__main__":
    main()
