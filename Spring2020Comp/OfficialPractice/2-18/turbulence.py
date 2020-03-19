lineOne = []
lineOneTemp = input()
lineOneTemp = lineOneTemp.split()

lineOne.append(int(lineOneTemp[0]))
lineOne.append(int(lineOneTemp[1]))

seats = []
seatsTemp = input()
seatsTemp = seatsTemp.split()

for i in range(len(seatsTemp)):
	seats.append(int(seatsTemp[i]))

numPass = lineOne[0]
currSeat = lineOne[1]

for i in range(len(lineTwo)):
    	if currSeat != seats[currSeat - 1]:
		temp = seats[currSeat - 1]
		seats[currSeat - 1] = currSeat
		currSeat = temp
		print(currSeat)

