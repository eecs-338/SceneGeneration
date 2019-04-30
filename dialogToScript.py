def findDialogue(str):
	str = str[1:]
	content = ""
	cind = 0
	while(True):
		if(str[cind] == '"'):
			break
		content += str[cind]
		cind += 1
	return content