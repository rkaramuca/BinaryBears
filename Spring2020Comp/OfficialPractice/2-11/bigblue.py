nl = int(input())
numBlues = 0
for i in range(nl):
    inS = input()
    inS = inS.split()
    for i in range(len(inS)):
        if inS[i] == "blue":
            numBlues += 1
    if numBlues >= len(inS) / 2:
        print("passed")
        numBlues = 0
    else:
        print("failed")
        numBlues = 0

