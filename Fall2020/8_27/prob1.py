#FIND OUT HOW TO GET LISTS OF THINGS WE CANNOT HAVE
#LOGIC IS FINE, FIND OUT LISTS

reserved = []
while(True):
	r = input()
	if(r=="LAST"):
		break
	else:
		reserved.append(r)
while(True):
	r = input()
	#works
	if(r=="END"):
		break
	else:
		l = 0
		print(l)
		while(l<len(cant1)):
			if(r[0] == cant1[l]):
				print('invalid')
			l += 1
