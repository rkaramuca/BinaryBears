for i in range(int(input())):
	x = input()
	x = x.split()
	l = int(x[0])
	w = int(x[1])
	print(f"Area={l*w} square inches; Perimeter={(l*2)+(w*2)} inches")
