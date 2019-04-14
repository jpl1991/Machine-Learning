def subString(string):

	substrings = set()

	while len(string)!=1:
		
		for s in range(1,len(string)+1):
			substrings.add(string[:s])

		string = string[1:]

	substrings.add(string)

	return substrings

s = subString("aaaa")

print(len(s))
