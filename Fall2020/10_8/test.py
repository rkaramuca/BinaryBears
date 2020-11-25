for i in range(int(input())):
	grade = input()
	grade = grade.split()
	if( float(grade[0]) > 2.5 and (grade[1] == 'A' or grade[1] == 'B' or grade[1] == 'C')):
		print("Eligible")
	else:
		print("Ineligible")
