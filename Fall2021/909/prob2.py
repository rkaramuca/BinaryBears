print(input())
x = input()
while '#' in x:
	print(x)
	x = input()
	
x=x.split()
print(x[1] + ' ' + x[0])
col=int(x[0])
row=int(x[1])
maxval = input()
print(maxval)

mat = []
for i in range(row):
	ele = input()
	rw = ele.split()
	rw=list(map(int, rw))
	mat.append(rw)

rotate = list(zip(*mat))
for i in rotate:
	r = ' '.join(map(str, i[::-1]))
	print(r)