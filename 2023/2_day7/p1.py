#!/usr/bin/python3

_str = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
_type = ["Five of a kind", "Four of a kind", "Full house", "Three of a kind",
         "Two pair", "One pair", "High card"]

class BinaryTreeNode:
    def __init__(self, data):
        self.hand = data[0]
        self.shand = sorted(self.hand, key=sortHandFnc)
        self.bet = int(data[1])
        self.h_type = getType(self.shand)
        self.leftChild = None
        self.rightChild = None

    def insert(self, hand):
        if compareHands(self, hand):
            if self.leftChild == None:
                self.leftChild = hand
            else:
                self.leftChild.insert(hand)
        else:
            if self.rightChild == None:
                self.rightChild = hand
            else:
                self.rightChild.insert(hand)

def compareHands(h1, h2):
    if h1.h_type < h2.h_type:
        return True
    elif h1.h_type == h2.h_type:
        for i in range(len(h1.hand)):
            h1v = _str.index(h1.hand[i])
            h2v = _str.index(h2.hand[i])
            if h1v < h2v:
                return True
            elif h1v > h2v:
                return False
    return False

def getType(h):
    t = {}
    for c in h:
        try:
            t[c] += 1
        except:
            t[c] = 1

    st = dict(sorted(t.items(), key=lambda item: item[1], reverse=True))
    three = False
    two = False
    for v in st.values():
        match v:
            case 5:
                return 0
            case 4:
                return 1
            case 3:
                three = True
            case 2:
                if three:
                    return 2
                if two:
                    return 4
                two = True
            case _ :
                if three:
                    return 3
                if two:
                    return 5
                return 6

def sortHandFnc(h):
    return _str.index(h)

def parseInput(fn):
    f = open(fn, "r")

    t_hands = None

    for h in f:
        hand = h.strip().split(" ")
        if len(hand) == 2:
            t_h = BinaryTreeNode(hand)
            if t_hands == None:
                t_hands = t_h
            else:
                t_hands.insert(t_h)

    f.close()
    return t_hands

def calcTotal(t_h, rank):
    total = 0
    r = rank
    if t_h.leftChild != None:
        total, r = calcTotal(t_h.leftChild, rank)
    tmp = r * t_h.bet
    total += tmp
    print((''.join(t_h.hand), tmp, r, _type[t_h.h_type], total))
    r += 1
    if t_h.rightChild != None:
        t, r = calcTotal(t_h.rightChild, r)
        total += t
    return (total, r)

def main():
    hands = parseInput("input")
    total = calcTotal(hands, 1)
    print(total)

if __name__ == "__main__":
    main()
