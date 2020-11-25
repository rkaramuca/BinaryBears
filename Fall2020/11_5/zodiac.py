signs = ['snake', 'horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'rabbit', 'dragon']

for i in range(int(input())):
	case = input()
	index = (int(case) - 1965) % 12
	print(f"{case} is the year of the {signs[index]}")
