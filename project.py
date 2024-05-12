from pyvis.network import Network
net = Network()


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
	mincount = 10
	for x in characters:
		if x[-1] == "s" and x[:-1] in characters:
			characters[x[:-1]] += characters[x]
			a.append(x)
		elif characters[x] <= mincount:
			a.append(x)
	for x in a:
		characters.pop(x)
	return characters

			 
bookname = "Harry Potter.txt"
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
	flag = False
	for x in meetings:
		if not flag or len(meetings[x]) > lmx:
			lmx = len(meetings[x])
			mx = x
			flag = True
		k += 1
		print(x, ":")
		for y in meetings[x]:
			print("    ", y, "-", meetings[x][y])
	character_to_idx = {}
	for idx, character in enumerate(meetings):
		character_to_idx[character] = idx
		if character == mx:
			net.add_node(idx, label=character, color = "#F36868", title = character)
		elif len(meetings[character]) > 12 and character != mx:
			net.add_node(idx, label=character, color = "#A1F5A1", title = character)
		else:
			net.add_node(idx, label=character, color = "#BEB7F7", title = character)
	
	for character in meetings:
		for other in meetings[character]:
			net.add_edge(character_to_idx[character], character_to_idx[other], weight=meetings[character][other])
	net.show_buttons(filter_=['physics'])
	net.show("visual.html")


	
	
		





