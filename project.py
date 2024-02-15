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
			if s[i][0] in m and i != 0:
				if s[i] not in characters:
					characters[s[i]] = 1
				else:
					characters[s[i]] += 1
	for x in characters:
		print(x, "-", characters[x])


