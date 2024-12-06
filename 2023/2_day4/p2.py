#!/usr/bin/python3

def parseInput(fn):
    f = open(fn, "r")

    game = []
    for r in f:
        try:
            a = r.split(":")
            #print(a)
            id = int(a[0].replace("Card ", ""))

            nums = a[1].replace("\n", "").split("|")
            winners = nums[0].strip().replace("  ", " ").split(" ")
            #print("winners: {}", winners)
            mine = nums[1].strip().replace("  ", " ").split(" ")
            #print("mine: {}", mine)

            card = { "id": id,
                    "winning": winners,
                    "mine": mine
                    }
            game.append(card)
        except:
            pass

    f.close()
    return game

def getMatches(cards):
    scores = {}
    for card in cards:
        matches = 0
        for m in card["mine"]:
            if m in card["winning"]:
                matches += 1
        scores[card["id"]] = { "id": card["id"],
                             "matches": matches,
                              "copies": 1
             }
    return scores

def getTotals(scores):
    total = 0
    for id, s in scores.items():
        total += s["copies"]
        for i in range(1, s["matches"]+1):
            if len(scores) >= id+i:
                scores[id+i]["copies"]+= s["copies"]

    return (scores, total)

def main():
    cards = parseInput("input")
    #print(cards)
    scores = getMatches(cards)
    #print(scores)
    (scores, total) = getTotals(scores)
    print(scores)
    print(total)
    print(len(scores))

if __name__ == "__main__":
    main()
