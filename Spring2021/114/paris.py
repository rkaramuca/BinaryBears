for i in range(int(input())):
	time = input()
	time = time.split('=')
	l = time[0]
	time = time[1].split(':')
	nt = 0
	if l == "Roanoke":
		nt = int(time[0]) + 6
		if nt > 23:
			nt = 22 - (int(time[0]) - 6)
		if nt < 12:
			print(f"The time in Paris is now {nt}:{time[1]} AM")
		else:
			print(f"The time in Paris is now {nt - 12}:{time[1]} PM")
	if l == "Paris":
		nt = int(time[0]) - 6
		if nt < 0:
			nt = 24 - (int(time[0]) + 6)
		if nt == 0:
			print(f"The time in Roanoke is now 12:{time[1]} AM")
		elif nt < 12:
			print(f"The time in Roanoke is now {nt}:{time[1]} AM")
		else:
			print(f"The time in Roanoke is now {nt - 12}:{time[1]} PM")
