#!/usr/bin/env python3

from pprint import pprint


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


def checkRules(rules, updates):
    printed = []
    toPrint = [int(x) for x in updates.split(',')]
    for print in toPrint:
        if print in rules:
            for before in rules[print]:
                if before not in printed and before in toPrint:
                    return False, print
        printed.append(print)

    return True, toPrint[int(len(toPrint)/2)]


def main():
    # rules, updates = parseInput("test")
    rules, updates = parseInput("input")
    newRules = parseRules(rules)
    pprint(newRules)
    sum = 0
    for update in updates:
        result, val = checkRules(newRules, update)
        print(result, val)
        if result:
            sum += val
    print(sum)


if __name__ == "__main__":
    main()
