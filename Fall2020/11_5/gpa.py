grades = {
	"A": 4,
	"B+": 3.5,
	"B": 3,
	"C+": 2.5,
	"C": 2,
	"D": 1,
	"F": 0,
	"S": 1,
	"U": 0
}
#x = grades["A"]
for i in range(int(input())):
	earned = 0
	credit = 0.0
	gpa = 0.0
	quality = 0.0
	case = input()
	case = case.split()
	for j in range(int(case[1])):
		curr = input()
		curr = curr.split()
		if(curr[1] == "S" ):
			earned += 1
		elif(curr[1] == "U"):
			earned += 0
		else:
			grade = grades[curr[1]]
			if( grade != 0 ):
				earned += int(curr[2])
			credit += float(curr[2])
			currQuality = grade * float(curr[2])
			quality += currQuality
	gpa = quality / credit
	
	#print(f"{case[0]} has earned {earned} hours with a GPA of {:0.2f}").format(gpa))
	print(str(case[0]) + " has earned " + str(earned) + " hours with a GPA of " + "{:0.2f}".format(gpa))
