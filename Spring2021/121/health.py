w = []
m = []
y = []

# what week is it
week = 0
# what month is it
month = 0

while(True):
	mi = input()
	mi = mi.split()
	mi = list(map(float, mi))

	for i in mi:
		if i != -1.0 and i != -2.0 and i != -3.0:
			w.append(i)
			m.append(i)
			y.append(i)
		elif i == -1.0:
			week += 1
			tot = sum(w)
			print(f"Week #{week} = {round((tot / len(w)), 2)} mi.")
			w.clear()
		elif i == -2.0:
			month += 1
			tot = sum(m)
			print(f"\nMonth #{month} = {round((tot / len(m)), 2)} mi.\n")
			m.clear()
		elif i == -3.0:
			tot = sum(y)
			print(f"\nYear to Date for {len(y)} days = {round((tot / len(y)), 2)} mi.\n")
			y.clear()
			break
	if i == -3.0:
		break
	
