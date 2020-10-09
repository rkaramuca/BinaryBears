n = int(input())
for i in range(n):
	x = input()
	x = x.split()
	#converts each index of x to binary number, hence ",2", then adds them together
	s = bin(int(x[0],2) + int(x[1],2))
	#bin adds 0b at the beginning of all binary outputs, so "[2::]" prints the output from after that index to give just the binary
	print((i+1), s[2::])

