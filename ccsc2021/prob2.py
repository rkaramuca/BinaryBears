for i in range(int(input())):
	delim = input().split()
	case = input()
	scase = case.split()
	print(case + " is balanced" if scase.count(delim[0]) == scase.count(delim[1]) else case + " is not balanced")
