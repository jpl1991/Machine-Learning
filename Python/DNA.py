def updateStr(strList):
	finallist = []
	validstr = "ATGC"
	for string in strList:
		if(len(string)>10 and len(string)<100):
			if(string.isupper()):
				characterlist = list(string)
				valid = True				
				for s in characterlist:
					if s not in validstr:
						valid = False
				if(valid==True):
					finallist.append(string)
	

	if(len(finallist)<3):
		return ""
	else:
		return finallist


def mergeStr(strList):

	start = []
	end = []
	dic = {}
	finalstr=''
	for string in strList:
		start.append(string[:3])
		end.append(string[-3:])
		dic[string[:3]] = string[3:]
	for string in strList:
		if(string[:3] not in end and string[-3:] in start):
			finalstr = string
	print(finalstr)
	while(dic.get(finalstr[-3:])!=None):
		finalstr += dic.get(finalstr[-3:])
	return finalstr


def report(string, condon_mapping):
	strlist=[]
	dic ={}
	finalstr =""
	for key,value in condon_mapping.items():
		dic[value] = 0
	if(len(string)>3):
		strlist = [string[i:i+3] for i in range(0, len(string), 3)]
		for string in strlist:
			if dic.get(condon_mapping.get(string))!=None:
				dic[condon_mapping.get(string)] +=1

	keys =list(dic.keys())
	keys.sort()
	for key in keys:
		finalstr+= key+": "+ str(dic.get(key))+"\n"

	return finalstr

input = ['AGTGGGGGGGGG', 'AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT', 'RRYYGGGCCCC','AAGCCCCttt']

output = updateStr(input)

mergeoutput = mergeStr(output)

print(mergeoutput)

condon_mapping = {'AAA':'Lysine','GGG':'Glycine','TTT':'Phenylalanine'}
final = report(mergeoutput, condon_mapping)

print(final)
