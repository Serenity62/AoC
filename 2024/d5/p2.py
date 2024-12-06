#!/usr/bin/env python3

def parseInput(fn):
    with open(fn, "r") as f:
        ls = f.read().strip()
        split = ls.split('\n\n')
        rules = split[0].split('\n')
        update = split[1].split('\n')

        return rules, update


def parseRules(rules):
    rf = {}
    for rule in rules:
        tmp = rule.split('|')
        tmp = [int(x) for x in tmp]
        if tmp[1] not in rf:
            rf[tmp[1]] = []
        rf[tmp[1]].append(tmp[0])
    return rf


def checkRules(rules, toPrint):
    printed = []
    for print in toPrint:
        if print in rules:
            for before in rules[print]:
                if before not in printed and before in toPrint:
                    return False, print
        printed.append(print)

    return True, toPrint[int(len(toPrint)/2)]


def fixOrder(rules, updates):
    toPrint = [x for x in updates]
    while True:
        print(toPrint)
        res, val = checkRules(rules, toPrint)
        if res:
            return toPrint, val
        toPrint.pop(toPrint.index(val))
        toPrint.append(val)


def main():
    # rules, updates = parseInput("test")
    rules, updates = parseInput("input")
    newRules = parseRules(rules)
    sum = 0
    fsum = 0
    for update in updates:
        tmp = [int(x) for x in update.split(',')]
        result, val = checkRules(newRules, tmp)
        if result:
            sum += val
        else:
            _res, v = fixOrder(newRules, tmp)
            fsum += v
    print('Correct', sum)
    print('Fixed', fsum)


if __name__ == "__main__":
    main()
