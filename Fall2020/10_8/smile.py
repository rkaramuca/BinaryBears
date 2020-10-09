iS = input()
smile = ""
smileCount = 0
for i in iS:
	if len(smile) == 3:
		smileCount += 1
		smile = ""
	if i == ':' and len(smile) == 0:
		smile += i 
	elif i == '-' and len(smile) == 1:
		smile += i
	elif i == ')' and len(smile) == 2:
		smile += i
	else:
		smile = ""
			
if len(smile) == 3:
	smileCount += 1
	smile = ""
print(smileCount)
