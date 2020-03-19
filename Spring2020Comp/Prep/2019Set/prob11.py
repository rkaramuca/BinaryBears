cases = int(input())

for i in range(cases):
    days = int(input())

    numT = []
    numTsplit = []

    mTotal = 0

    for i in range(days):
        numT.append(input())

    for i in range(days):
        toSplit = numT[i]
        numTsplit.append(toSplit)

    toCheck = ""

    day = 0
    
    for i in range(days):
        toCheck = numTsplit[i]
        toCheck = toCheck.split()
        
        if day == 0:
            mTotal += int(toCheck[0])
            day += 1
        elif day == 1:
            mTotal += int(toCheck[2])
            day += 1
        elif day == 2:
            mTotal += int(toCheck[1])
            day += 1
        elif day == 3:
            mTotal += int(toCheck[0])
            day = 1
            
        toCheck.clear()

    print(mTotal)
