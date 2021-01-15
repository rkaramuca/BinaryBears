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

	out = out.replace('$', word)
	
	out = out.replace('%', "")
	out = out.replace('@', "")
	out = out.replace('$', "")
	out = out.replace('#', "")
	out = out.strip()
	out = " ".join(out.split())
	print(out)
