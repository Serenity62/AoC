#!/usr/bin/python3

def parseInput(fn):
    f = open(fn, "r")

    game = []
    for r in f:
        try:
            a = r.split(":")
            #print(a)
            id = a[0].replace("Card ", "")

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

def getScore(cards):
    scores = []
    for card in cards:
        matches = 0
        score = 0
        for m in card["mine"]:
            if m in card["winning"]:
                matches += 1
        if matches > 0:
            score = pow(2, matches -1)
        s = { "id": card["id"],
             "matches": matches,
             "score": score
             }
        scores.append(s)
    return scores

def getTotal(scores):
    total = 0
    for s in scores:
        total += s["score"]

    return total

def main():
    cards = parseInput("input")
    #print(cards)
    scores = getScore(cards)
    print(scores)
    total = getTotal(scores)
    print(total)

if __name__ == "__main__":
    main()
