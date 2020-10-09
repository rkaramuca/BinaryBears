import math

for _ in range(int(input())):
	case = input()
	case = int(case)
	inc=1
	if case == 0:
		print('H')
	else:
		while True:
			if ( (2**inc) + (inc - 1) == case):
				break
			elif ( (2**inc) + (inc - 1) > case):
				inc = 0
				break
			inc+=1
		s = ""
		if inc != 0:
			if s=="":
				s+='H'
			for i in range(inc):
				if(s[i] == 'A'):
					s+='H'
				else:
					s+='A'
			print(s)
