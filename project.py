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
	sep = [".", "!", "?"]
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
characters = []
for x in sentences:
	s = wordsfroms(x)
	for i in range(len(s)):
		if s[i][0] in m and i != 0:
			characters.append(s[i])
print(*characters)


