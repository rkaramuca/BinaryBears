for i in range(int(input())):
	case = input()
	if "Simon says" in case:
		print(f"{case[10::]}")
