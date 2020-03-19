labs = []
hw = []
projects = []
exams = []

in1 = input()

in1 = in1.split()

lp = int(in1[0])
hp = int(in1[1])
pp = int(in1[2])
ep = int(in1[3])
na = int(in1[4])
lt = 0
ht = 0
pt = 0
et = 0
nl = 0
nh = 0
np = 0
ne = 0

for i in range(na):
    ca = input()
    if "Lab" in ca:
        labs.append(ca)
    elif "Hw" in ca:
        hw.append(ca)
    elif "Proj" in ca:
        projects.append(ca)
    elif "Exam" in ca:
        exams.append(ca)

for i in range(len(labs)):
    temp = labs[i].split()
    curr = temp[2].split("/")
    lt += int(curr[0]) / int(curr[1])
    nl += 1
for i in range(len(hw)):
    temp = hw[i].split()
    curr = temp[2].split("/")
    ht += int(curr[0]) / int(curr[1])
    nh += 1
for i in range(len(projects)):
    temp = projects[i].split()
    curr = temp[2].split("/")
    pt += int(curr[0]) / int(curr[1])
    np += 1
for i in range(len(exams)):
    temp = exams[i].split()
    curr = temp[2].split("/")
    et += int(curr[0]) / int(curr[1])
    ne += 1

# total grade for each category = total currently / number of said category * percent worth for that assignment
lt = (lt / nl) * lp
ht = (ht / nh) * hp
pt = (pt / np) * pp
et = (et / ne) * ep

# round to get the number to a whole integer
total = round(lt + ht + pt + et)
print(total)



