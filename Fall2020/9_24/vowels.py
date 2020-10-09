from itertools import permutations

cases = input()
cases = int(cases)

perms = []
name = ""
vowels = ['a', 'e', 'i', 'o', 'u']

def vowelSwap(numVowels, vFound):

for i in range(cases):
	name = input()
	found = []
	vCount = 0
	for letter in name:
		if letter in vowels:
			vCount += 1
			found.append(letter)
			name.replace(letter, '/')
	print(name)
	vowelSwap(vCount, found)

for perm in perms:
	print(perm)
