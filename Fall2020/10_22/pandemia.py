def infected(s):
    if not '0' in s and not '1' in s:
        return 0
    if not '1' in s:
        return 0
    if not 'X' in s and '1' in s:
        return 100
    inf = 0
    nof = 0
    sp = s.split('X')
    for cont in sp:
        for i in cont:
            if i == '1':
                inf += len(cont)
                break
        for j in cont:
            if i == '0':
                nof += 1
    if inf+nof == 0:
        return 0
    else:
        return 100*(inf/(inf+nof))

s="X00X000000X10X0100"
print(infected(s))
