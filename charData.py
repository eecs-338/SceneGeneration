def newCharList():
	charList = {}
	return charList

def newChar(charList, name):
	charList[name] = {}
	return charList

def addAttribute(charList, name, attr):
	attr_dict = charList[name]
	attr_dict[attr] = []
	charList[name] = attr_dict
	return charList

def delAttribute(charList, name, attr):
	attr_dict = charList[name]
	attr_dict.pop(attr)
	charList[name] = attr_dict
	return charList
	
def addValuesForAttribute(charList, name, attr, val):
	attr_dict = charList[name]
	attr_vals = attr_dict[attr]
	attr_vals.append(val)
	attr_dict[attr] = attr_vals
	charList[name] = attr_dict
	return charList