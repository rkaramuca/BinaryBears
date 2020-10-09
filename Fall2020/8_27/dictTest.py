#actors = {"Kevin Bacon": 0}
#print(actors["Kevin Bacon"])
#actors["Kevin Bacon"] += 1
#print(actors["Kevin Bacon"])

n = int(input())
actors={}
for i in range(n):
	#filling actors correctly
	a = input()
	a = a.split()
	b1 = 0
	b2 = 0
	a1 = a[0] + " " + a[1]
	a2 = a[2] + " " + a[3]
	if(a1 in actors):
		print("Found")
	if(a1 == "Kevin Bacon"):
		b2 += 1
	if(a2 == "Kevin Bacon"):
		b1 += 1
	actors.update({a1: b1, a2: b2})
		
print(actors)
