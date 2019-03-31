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
    strlist = list(strList)
    ends = [s[-3:] for s in strlist]
    heads = [s[:3] for s in strlist]
    final = ''
    ending = []
    print(strlist)
    for string in strList:   
        print(string)
        if(string[:3] not in ends and string[-3:] in heads):
            final = string
            strlist.remove(string)
        elif (string[:3] in ends and string[-3:] not in heads):
            ending.append(string)
            strlist.remove(string)
    print(strlist)
    stop = False
    while stop == False:
        stop = True
        for string in strlist:
            if final[-3:] == string[:3]:
                final += string[3:]
                strlist.remove(string)
                stop = False
                break
    
    print(ending)
    
    for string in ending:
        if final[-3:] == string[:3]:
            final+= string[3:]
            
    return final    


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

input = ['AATTGGCCAATTG', 'TTGAATTGGCCAAAA', 'AAATTTGGGCCC', 'AAAEEERRRTTT','AATACCCCCGGG', 'NEWUSER123']

output = updateStr(input)

mergeoutput = mergeStr(output)

print(mergeoutput)

condon_mapping = {'AAA':'Lysine','GGG':'Glycine','TTT':'Phenylalanine'}
final = report(mergeoutput, condon_mapping)

print(final)
