air = [30, 25, 18, 12, 5, -10]
ratio = [10, 15, 20, 30, 40, 50]
locs = []
water = []

for i in range(int(input())):
	curr = input()
	curr = curr.split()
	snow = float(curr[0])
	temp = int(curr[1])
	loc = curr[2::] 
	loc = ' '.join(loc)
	locs.append(loc)
	m = min(air, key=lambda x:abs(x-temp))
	i = air.index(m)
	rat = ratio[i]
	w = float(snow * (1 / rat))
	w = round(w, 1)
	water.append(w)
wmax = max(water) 
i = water.index(wmax)
print(f"More water fell in {locs[i]} ({wmax} inches)")
