words = []
medi = ""

while(True):
	try:
		curr = input()
		curr = curr.split()
		for i in curr:
			i = i.strip().lower()
			i = ''.join([j for j in i if j.isalpha()])
			words.append(i)
	except EOFError as error:
		words.sort()
		med = int(len(words) / 2)
		modes = []
		mode = 0
		for i in words:
			if words.count(i) > mode:
				modes.clear()
				mode = words.count(i)
				modes.append(i)
			elif words.count(i) == mode and i not in modes:
				modes.append(i)
		ms = "["
		for i in modes:
			ms += i
			ms += " ("
			ms += str(words.count(i))
			ms += ")$"
		ms = ms[:len(ms) - 1] + '' + "]"
		ms = ms.replace('$', ',')
		if med % 2 == 0:
			medi += words[med - 1]
			medi += " "
			medi += words[med]
			medians = ','.join(medi.split())
			print(f"My median=[{medians}]")
			print(f"My mode={ms}")
		else:
			median = words[med]
			print(f"My median=[{median}]")
			print(f"My mode={ms}")
		break
