#possible solution --> check extraneous solutions
import math
cases = int(input())
for i in range(cases):
    rawIn = input()
    rawIn = rawIn.split()
    d = int(rawIn[0])
    s = int(rawIn[1])

    if d > s or d == s:
        answer = (math.log(d) - math.log(s)) + 1
    elif s > d:
        answer = (d / s) 
    print(round(answer, 2))

