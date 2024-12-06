#!/usr/bin/python3

class LL:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.root = self

    def insert(self, node):
        if self.next == self.root:
            node.root = self.root
            node.next = self.root
            self.next = node
        else:
            self.next.insert(node)

    def print(self):
        tmp = self.data
        if self.next != self.root:
            tmp = ''.join([tmp, self.next.print()])
        return tmp

def parseInput(fn):
    f = open(fn, "r")

    lines = f.read().strip().replace("\n\n", "\n").split("\n")
    dl = lines[0]
    #print(lines)
    dn = None
    for d in dl:
        if dn == None:
            dn = LL(d)
        else:
            dn.insert(LL(d))
    
    map = {}
    for m in lines[1:]:
        t = m.split(" = ")
        #print(t)
        key = t[0]
        path = t[1].replace("(", "").replace(")", "").split(", ")
        #print(path)
        map[key] = path

    f.close()
    return (dn, map)

def steps(d, m):
    s = 1
    p = "AAA"
    while True:
        match d.data:
            case "L":
                p = m[p][0]
            case "R":
                p = m[p][1]
        if p == "ZZZ":
            break
        d = d.next
        s += 1

    return s

def main():
    (directions, map) = parseInput("input")
    #print(directions.print(), map)
    s = steps(directions, map)
    print(s)

if __name__ == "__main__":
    main()
