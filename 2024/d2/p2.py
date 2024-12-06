#!/usr/bin/env python3

def parseInput(fn):
    reports = []
    with open(fn, "r") as f:
        ls = f.read().strip()
        for report in ls.split('\n'):
            reports.append([int(x) for x in report.strip().split(' ')])

        return reports


def isSafe(report):
    if len(report) == 0:
        return False
    prv = None
    inc = None
    for lvl in report:
        if prv is not None:
            diff = prv - lvl
            if abs(diff) < 1 or abs(diff) > 3:
                return False
            if inc is None:
                inc = diff > 0
            elif (inc and diff < 0) or (not inc and diff > 0):
                return False
        prv = lvl
    return True


def check(report):
    if isSafe(report):
        return True
    for idx in range(len(report)):
        tmp = [x for x in report]
        tmp.pop(idx)
        if isSafe(tmp):
            return True
    return False


def main():
    # reports = parseInput("test")
    reports = parseInput("input")
    cnt = 0
    for report in reports:
        safe = check(report)
        print(safe)
        if safe:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
