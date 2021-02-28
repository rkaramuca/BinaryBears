speeds = []
miles = []
for i in range(int(input())):
    case = input()
    case = case.split()
    speeds.append(int(case[0]))
    miles.append(int(case[1]))

integralSpeed = 0

for i in range(len(speeds)):
    if i <= len(speeds) - 2:
        sDiff = speeds[i + 1] - speeds[i]
        mDiff = miles[i + 1] - miles[i]
        if mDiff // sDiff > integralSpeed:
            integralSpeed = mDiff // sDiff

print(integralSpeed)
