def wordsfroms(s):
	sep = ' ,:".!;?\n-'
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


def get_stopwords():
	with open("stopwords.txt") as f:
		return {word.strip() for word in f.readlines()}

stopwords = get_stopwords()			 
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
			if k and k[0] in m and i != 0 and k.lower() not in stopwords:
				if k not in characters:
						characters[k] = 1
				else:
					characters[k] += 1
	a = []
	for x in characters:
		if x[-1] == "s" and x[:-1] in characters:
			characters[x[:-1]] += characters[x]
			a.append(x)
		elif characters[x] <= 10:
			a.append(x)
	for x in a:
		characters.pop(x)
	meatings = {}
	for x in sentences:
		m = set()
		s = wordsfroms(x)
		for word in s:
			if word in characters:
				m.add(word)
		for ch in m:
			if len(m) > 1:
				if ch not in meatings:
					meatings[ch] = m
				else:
					meatings[ch] |= m
for x in meatings:
	meatings[x].remove(x)
k = 0
for x in meatings:
	print(x, ":")
	for y in meatings[x]:
		print("    ", y)
	k += 1
	if k > 3:
		break




