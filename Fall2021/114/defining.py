pref = {
	"anti" : "against",
	"post" : "after",
	"pre" : "before",
	"re" : "again",
	"un" : "not"
}

suf = {
	"er" : "one who",
	"ing": "to actively",
	"ize": "change into",
	"s" : "multiple instances of",
	"tion" : "the process of"
}

for i in range(int(input())):
	word = input()
	out = "% @ $ #"
	preL = word[0:4]
	pL = ""
	#starts at the beginning of the word and checks for a prefix (start at 0 and increment to 4, the largest prefix size)
	for i in range(len(preL)):
		pL += preL[i]
		if pL in pref:
			if pL == "re":
				word = word[2:]
				out = out.replace("#", pref[pL])
				break
			else:
				word = word[i + 1:]
				out = out.replace("%", pref[pL])
				break

	#check if a length-4, 3, 2, or 1 suffix exists in the suf dictionary
	if word[-4:] in suf:
		suff = word[-4:]
		word = word[0:-4]
		word += "ing"
		out = out.replace("%", suf[suff])
	elif word[-3:] in suf:
		suff = word[-3:]
		word = word[0:-3]
		out = out.replace("@", suf[suff])
	elif word[-2:] in suf:
		suff = word[-2:]
		out = out.replace("@", suf[suff])
		word = word[0:-2]
		word += "s"
	elif word[-1:] in suf:
		suff = word[-1:]
		out = out.replace("@", suf[suff])
		word = word[0:-1]

	#replace the $ position with the re-written word (word w/o prefix or suffix)
	out = out.replace('$', word)
	
	#replace any left-over symbols with blanks, then strip spaces
	out = out.replace('%', "")
	out = out.replace('@', "")
	out = out.replace('$', "")
	out = out.replace('#', "")
	out = out.strip()
	#split the string by spaces then rejoin it with spaces between each element
	out = " ".join(out.split())
	print(out)
