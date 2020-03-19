numsIn = input()
numsIn = numsIn.split()
numsList = []

for i in range(len(numsList)):
    numsList[i] = int(numsList[i])

n = int(numsIn[0])
m = int(numsIn[1])
a = int(numsIn[2])
c = int(numsIn[3])
x = int(numsIn[4])

currentNum = x

for i in range(n):
    toAdd = ((a * currentNum) + c) % m
    currentNum = toAdd
    numsList.append(toAdd)

foundCounter = 0

def binarySearch(numList, key):
    first = 0
    last = len(numList) - 1
    middle = 0
    location = 0
    found = False
    global foundCounter
    
    while ((not found) and (first <= last)):
        middle = int((first + last) / 2)

        if key == numList[middle]:
            found = True
        elif key < numList[middle]:
            last = middle - 1
        else:
            first = middle + 1
    location = middle
    if found:
        foundCounter += 1

for i in range(n):
    binarySearch(numsList, numsList[i])

print(foundCounter)




    


