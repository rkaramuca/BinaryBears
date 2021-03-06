case = input()
chars = []
unique = True
for i in case:
    if not i in chars:
        chars.append(i)
    else:
        unique = False
        break
if unique:
    print('1')
else:
    print('0')
    

