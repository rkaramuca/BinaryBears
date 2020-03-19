su = []
us = []
counter = 0 

suPs = input()
usPs = input()

suS = suPs.split()
usS = usPs.split()

suS.sort()
usS.sort()

for i in range(5):
    su.append(int(suS[i]))
    us.append(int(usS[i]))

for i in range(5):
    if su[i] > us[i]:
        counter += 1

print(counter)
