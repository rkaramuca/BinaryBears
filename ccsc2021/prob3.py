mats = {
	"velvet":  .25,
	"straw": .35,
	"wool": .45
}

for i in range(int(input())):
	hat = input()
	hat = hat.split()
	model = hat[1]
	mat = hat[2]
	s = hat[3::]
	size = float(s[0])
	if len(s) > 1:
		size += float((float(s[1][0]) / float(s[1][2])))
	
	cir = (25/8) * size
	r = cir / (2 * 3.14159)
	top = 3.14159 * (r ** 2)
	mid = 2 * 3.14159 * r * 4
	brim = (3.14159 * ((r + 3) ** 2)) - (3.14159 * (r ** 2))	
	area = top + mid + brim
	
	cost = area * mats[mat]
	print(f"Model {model} $ {round(cost,2)}")
