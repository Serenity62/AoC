#!/usr/bin/env python3

def parseInput(fn):
    with open(fn, "r") as f:
        ls = f.read().strip()

        return ls


def main():
    t = parseInput("test")
    print(t)


if __name__ == "__main__":
    main()
