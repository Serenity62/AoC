#!/usr/bin/env python3

def parseInput(fn):
    field = []
    start = (0, 0)
    direction = '^'
    with open(fn, "r") as f:
        ls = f.read().strip()
        for line in ls.split('\n'):
            tmp = []
            for char in line:
                if char in ['^', '>', '<', 'v']:
                    start = (len(field), len(tmp))
                    direction = char
                tmp.append(char)
            field.append(tmp)
    return field, start, direction


def printField(field):
    for r in field:
        print(''.join(r))
    print('')


def run(field, start, direction):
    field[start[0]][start[1]] = 'X'
    pos = start
    steps = 0
    distinct = 1
    translator = {
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }
    rotate = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }
    while True:
        i, j = pos
        ip, jp = translator[direction]
        inxt, jnxt = i + ip, j + jp
        if inxt < 0 or inxt >= len(field) or jnxt < 0 or jnxt >= len(field[0]):
            printField(field)
            return steps, distinct
        elif field[inxt][jnxt] == '#':
            direction = rotate[direction]
        else:
            if field[inxt][jnxt] != 'X':
                distinct += 1
            pos = (inxt, jnxt)
            field[inxt][jnxt] = 'X'
            steps += 1


def main():
    # field, start, direction = parseInput("test")
    field, start, direction = parseInput("input")
    steps = run(field, start, direction)
    print(steps)


if __name__ == "__main__":
    main()
