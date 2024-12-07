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


def run(field, start, direction):
    pos = start
    steps = 0
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
    while steps < 99999:
        i, j = pos
        ip, jp = translator[direction]
        inxt, jnxt = i + ip, j + jp
        if inxt < 0 or inxt >= len(field) or jnxt < 0 or jnxt >= len(field[0]):
            return True
        elif field[inxt][jnxt] in ['#', 'O']:
            direction = rotate[direction]
        else:
            pos = (inxt, jnxt)
            steps += 1
    return False


def findLoops(field, start, direction):
    loops = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            tmp = field[i][j]
            if tmp == '.':
                field[i][j] = 'O'
                if not run(field, start, direction):
                    loops += 1
                field[i][j] = '.'
    return loops


def main():
    # field, start, direction = parseInput("test")
    field, start, direction = parseInput("input")
    print(findLoops(field, start, direction))


if __name__ == "__main__":
    main()
