def newCharList():
	charList = {}
	return charList

def newChar(charList, name):
	charList[name] = []
	return charList

def addAttribute(charList, name, attr):
	attr_list = charList[name]
	attr_list.append(attr)
	charList[name] = attr_list
	return charList

def delAttribute(charList, name, attr):
	attr_list = charList[name]
	del_list = []
	for a in attr_list:
		if(a != attr):
			del_list.append(a)
	charList[name] = del_list
	return charList