def wordsfroms(s):
	sep = ' ,:".!?'
	s += " "
	word = ""
	w = []
	for c in s:
		if c not in sep:
			word += c
		else:
			if word != "":
				w.append(word)
			word = ""
	return w


with open("test.txt", "r") as f:
	m = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	ch = []
	for line in f:
		a = wordsfroms(line)
		for x in a:
			if x[0] in m:
				ch.append(x)
print(*ch)
