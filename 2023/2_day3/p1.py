#!/usr/bin/python3

def parseInput():
    f = open("input", "r")

    engine = []

    for r in f:
        a = []
        for c in r:
            if c != "\n":
                a.append(c)
        engine.append(a)

    f.close()
    return engine

def isSymbol(c):
    valid_symbols ="!@#$%^&*(){}[]-=_+`~/?\\|;:'\"<>,"
    if c in valid_symbols:
        return True
    return False

def getPart(r, idx):
    pn = int(r[idx])
    print(r)
    sslice = r[:idx]
    sslice = sslice[::-1]
    print("Start: {}".format(sslice))
    bslice = r[idx+1:]
    print("End: {}".format( bslice))
    for i, c in enumerate(sslice):
        if c.isdigit():
            pn = int(c) * pow(10,i+1) + pn
        else:
            break
    #print(pn)
    for i, c in enumerate(bslice):
        if c.isdigit():
            pn = pn * 10 + int(c)
        else:
            break
    #print(pn)
    return pn

def findParts(e):
    parts = []
    ilen = len(e)

    for i, r in enumerate(e):
        jlen = len(r)
        for j, c in enumerate(r):
            if isSymbol(c):
                try:
                    if e[i-1][j].isdigit():
                        part = { "pn": getPart(e[i-1], j), "symbol": c }
                        parts.append(part)
                    else:
                        try:
                            if e[i-1][j-1].isdigit():
                                part = { "pn": getPart(e[i-1], j-1), "symbol": c }
                                parts.append(part)
                        except:
                            pass
                        try:
                            if e[i-1][j+1].isdigit():
                                part = { "pn": getPart(e[i-1], j+1), "symbol": c }
                                parts.append(part)
                        except:
                            pass
                except:
                    pass
                try:
                    if e[i+1][j].isdigit():
                        part = { "pn": getPart(e[i+1], j), "symbol": c }
                        parts.append(part)
                    else:
                        try:
                            if e[i+1][j-1].isdigit():
                                part = { "pn": getPart(e[i+1], j-1), "symbol": c }
                                parts.append(part)
                        except:
                            pass
                        try:
                            if e[i+1][j+1].isdigit():
                                part = { "pn": getPart(e[i+1], j+1), "symbol": c }
                                parts.append(part)
                        except:
                            pass
                except:
                    pass
                try:
                    if e[i][j-1].isdigit():
                        part = { "pn": getPart(e[i], j-1), "symbol": c }
                        parts.append(part)
                except:
                    pass
                try:
                    if e[i][j+1].isdigit():
                        part = { "pn": getPart(e[i], j+1), "symbol": c }
                        parts.append(part)
                except:
                    pass

                """
                for x in range(-1,2):
                    for y in range(-1,2):
                        ix = i + x
                        jy = j + y
                        try:
                            print("ix: {} jy: {}".format(ix, jy))
                            a = e[ix][jy]
                            if a.isdigit():
                                part = { 
                                    "pn": getPart(e[ix], jy),
                                    "symbol": c
                                }
                                parts.append(part)
                                if i == 1 or i == -1:
                                    break
                        except:
                            pass
                """
    return parts

def main():
    engine = parseInput()
    parts = findParts(engine)
    
    s = 0
    for p in parts:
        s += p["pn"]
    print("===================================")
    print(parts)
    print(s)

if __name__ == "__main__":
    main()
