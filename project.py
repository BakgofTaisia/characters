def wordsfroms(s):
	sep = ' ,:-"—.!;…?\n'
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
	

def get_characters(sentences):
	stopwords = get_stopwords()	
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
	mincount = 100
	for x in characters:
		if x[-1] == "s" and x[:-1] in characters:
			characters[x[:-1]] += characters[x]
			a.append(x)
		elif characters[x] <= mincount:
			a.append(x)
	for x in a:
		characters.pop(x)
	return characters

			 
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
	characters = get_characters(sentences)
	meetings = {}
	for x in sentences:
		m = set()
		s = wordsfroms(x)
		for word in s:
			if word in characters:
				m.add(word)
		for n1 in m:
			m1 = m.copy()
			m1.remove(n1)
			if n1 not in meetings:
				meetings[n1] = {}
			for nx in m1:
				if nx not in meetings[n1]:
					meetings[n1][nx] = 1
				else:
					meetings[n1][nx] += 1
	k = 0
	for x in meetings:
		k += 1
		print(x, ":")
		for y in meetings[x]:
			print("    ", y, "-", meetings[x][y])
		





