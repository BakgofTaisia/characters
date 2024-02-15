def wordsfroms(s):
	sep = ' ,:".!?\n-'
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


def checkapo(x):
	if  "’" in x:
		for i in range(len(x)):
			if x[i] == "’":
				x = x[:i]
				break
	return x

bookname = input()
with open(bookname, "r") as f:
	sep = ['.', '!', '?', '”', '“']
	sentences = []
	sen = ""
	for x in f.read():
		if x not in sep:
			sen += x
		else:
			if sen != "":
				sentences.append(sen)
			sen = ""
	m = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	characters = {}
	for x in sentences:
		s = wordsfroms(x)
		for i in range(len(s)):
			k = checkapo(s[i])
			if k[0] in m and i != 0:
				if k not in characters:
					characters[k] = 1
				else:
					characters[k] += 1
	for x in characters:
		print(x, "-", characters[x])


