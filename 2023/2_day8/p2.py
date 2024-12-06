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
    
    sns = []
    map = {}
    for m in lines[1:]:
        t = m.split(" = ")
        #print(t)
        key = t[0]
        if key[-1] == "A":
            sns.append(key)
        path = t[1].replace("(", "").replace(")", "").split(", ")
        #print(path)
        map[key] = path

    f.close()
    return (dn, map, sns)

def steps(d, m, sns):
    s = 1
    p = sns
    end = False
    while not end:
        end = True
        print(s, p)
        for i in range(len(p)):
            match d.data:
                case "L":
                    p[i] = m[p[i]][0]
                case "R":
                    p[i] = m[p[i]][1]
            if p[i][-1] != "Z":
                end = False
        if not end:
            d = d.next
            s += 1

    return s

def main():
    (directions, map, sns) = parseInput("input")
    #print(directions.print(), map)
    #print(sns)
    s = steps(directions, map, sns)
    print(s)

if __name__ == "__main__":
    main()
