info = input()
info = info.split()
numCards = int(info[0])
desire = int(info[1])

cards = input()
cardsStr = cards.split()
cardsInt = [int(n) for n in cards.split()]

pairs = {
    "1": "1",
    "2": "2",
    "5": "5",
    "6": "9",
    "8": "8",
    "9": "6",
    "0": "0"
}

def flip(card):
    flip = ""
    for i in card:
        if i in pairs:
            flip += pairs[i]
        else:
            flip = ""
    if flip != "":
        return flip[::-1]
    return ""

i = 0
j = 1

works = False
while i < len(cardsStr):
    if works:
        break
        
    while j < len(cardsStr):
        if works:
            break
        if flip(cardsStr[i]) != "" and flip(cardsStr[j]) != "":
            if cardsInt[i] + cardsInt[j] == desire or int(flip(cardsStr[i])) + cardsInt[j] == desire or cardsInt[i] + int(flip(cardsStr[j])) == desire or int(flip(cardsStr[i])) + int(flip(cardsStr[j])) == desire:
                works = True
            else:
                works = False
        elif flip(cardsStr[i]) != "" and flip(cardsStr[j]) == "":
            if cardsInt[i] + cardsInt[j] == desire or int(flip(cardsStr[i])) + cardsInt[j] == desire:
                works = True
            else:
                works = False
        elif flip(cardsStr[i]) == "" and flip(cardsStr[j]) != "":
            if cardsInt[i] + cardsInt[j] == desire or cardsInt[i] + int(flip(cardsStr[j])) == desire:
                works = True
            else:
                works = False
        elif flip(cardsStr[i]) == "" and flip(cardsStr[j]) == "":
            if cardsInt[i] + cardsInt[j] == desire:
                works = True
            else:
                works = False
        j += 1
    i += 1

if works:
    print("YES")
else:
    print("NO")
