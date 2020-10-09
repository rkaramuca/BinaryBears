for _ in range(int(input())):
	letters = []
	sent = input()
	sent = sent.lower()
	for letter in sent:
		if not letter in letters:
			if letter.isalpha():
				letters.append(letter)
	print( 26 - len(letters ) )
