#!/usr/bin/env python3

def parseInput(fn):
    tests = []
    with open(fn, "r") as f:
        ls = f.read().strip()
        for line in ls.split('\n'):
            tmp = line.split(': ')
            tests.append((int(tmp[0]), [int(x) for x in tmp[1].split(' ')]))
    return tests


def runTest(test):
    opers = ['+', '*']
    res, vals = test
    if len(vals) == 0:
        return False
    elif len(vals) == 1:
        return res == vals[0]
    for oper in opers:
        tmp = vals[1:]
        if oper == '+':
            tmp[0] = vals[0] + tmp[0]
        elif oper == '*':
            tmp[0] = vals[0] * tmp[0]
        result = runTest((res, tmp))
        if result:
            return True
    return False


def main():
    # t = parseInput("test")
    t = parseInput('input')
    sum = 0
    for test in t:
        if runTest(test):
            res, _ = test
            sum += res
    print(sum)


if __name__ == "__main__":
    main()
