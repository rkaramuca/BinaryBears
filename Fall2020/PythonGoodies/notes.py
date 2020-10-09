"binary bears".rfind('a') # returns last occurrence of that letter
"binary bears".count('b') # returns number of that letter seen
l = [1, 2, 3, 4]
print(["Case " + str(num) for num in l])

a = ['work', 'play', 'eat']
a = list( map(lambda x: x+"ing", a) )

#or

def add_suffix(s):
	return s+"ing"

a = list( map(add_suffix, a) )

def factors(n):
	f = [i for i in range(2, n//2) if n%i==0]
	f.append(n)
	return f

def memoize(F):
	hashed_states = {}
	def memoized_F(*args):
		if args not in hashed_states:
			hashed_states[args] = F(*args)
		return hashed_states[args]
	return memoized_F
