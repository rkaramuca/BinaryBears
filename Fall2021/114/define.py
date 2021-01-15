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
	out = ""
	if word[0:4] in pref:
		preff = word[0:4]
		out += pref[preff]
		out += " "
	elif word[0:3] in pref:
		preff = word[0:3]
		out += pref[preff]
		out += " "
	elif word[0:2] in pref:
		if word[0:3] == "pre":
			preff = word[0:3]
			out += pref[preff]
			out += " "
		if word[0:2] == "re":
			preff = word[0:2]
			out += " "
			out += pref[preff]
		else:
			preff = word[0:2]
			out += pref[preff]
			out += " "
	elif word[-4:] in suf:
		suff = word[-4:]
		out += suf[suff]
		out += " "
		out += word[0:-3]
		out += "ing"
	elif word[-3:] in suf:
		suff = word[-3:]
		out += suf[suff]
		out += " "
		out += word[0:-3]
	elif word[-2:] in suf:
		suff = word[-2:]
		out += suf[suff] 
		out += " "
		out += word[0:-2]
		out += "s"
	elif word[-1:] in suf:
		suff = word[-1:]
		out += suf[suff]
		out += " "
		out += word[0:-1]
		
	
