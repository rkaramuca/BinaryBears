menu = {
	'A': ["Hamburger", .25],
	'B': ["Cheeseburger", .3],
	'C': ["Chili Dog", .35],
	'D': ["Sub Sandwich", .65],
	'E': ["Baked Pizza", .75],
	'F': ["French Fries", .25],
	'G': ["Pepsi-Cola", .25],
	'H': ["Orange Soda", .15],
	'I': ["Hot Coffee", .10],
	'J': ["Milk", .15],
	'K': ["Apple Pie", .30],
	'L': ["Frosty Shake", .40],
	'M': ["Popcorn", .15]
}
order = 1
while True:
	# All input
	y = input()
	if y == "0 Z":
		break
	x = y.split()
	print(f"ORDER {order}")
	total = 0.0
	ntotal = 0.0
	
	# Separate orders
	while not '0' in x:
		print(f"{x[0]} {menu[x[1]][0]}")
		total += int(x[0]) * menu[x[1]][1]
		curr = menu[x[1]][1]
		for i in range(50):
			curr *= 1.03
		ntotal += curr * int(x[0])
		y = input()
		x = y.split()
		if '0' in x:
			print(f"ORDER {order} TOTAL in 1957 = ${round(total, 2):.2f}")
			print(f"ORDER {order} TOTAL in 2007 = ${round(ntotal, 2):.2f}")
	
	order += 1
	if y == "0 Z":
		break
	print()
