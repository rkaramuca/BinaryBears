for i in range(int(input())):
	case = input()
	case = case.split()
	for n in range(len(case)):
		case[n] = int(case[n])
	print(case[0] * case[1])
		
