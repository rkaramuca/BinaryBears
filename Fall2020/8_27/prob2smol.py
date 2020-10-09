for i in range(int(input())):
	x = input().split()
	print((i+1), bin(int(x[0],2)+int(x[1],2))[2::])
