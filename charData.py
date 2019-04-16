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
	
def charMember(charList, name):
	if name in charList:
		return True
	else:
		return False
		
def attrMember(charList, name, attr):
	attr_dict = charList[name]
	if attr in attr_dict:
		return True
	else:
		return False
		
def inheritAttributes(charList, parent, child):
	p_attr_dict = charList[parent]
	c_attr_dict = charList[child]
	
	for attr, vals in p_attr_dict:
		if attr in c_attr_dict:
			attr_vals = c_attr_dict[attr]
			attr_vals = flatAppend(attr_vals, vals)
			c_attr_dict[attr] = attr_vals
		else:
			c_attr_dict[attr] = vals
	
	charList[child] = c_attr_dict
	return charList


def flatAppend(lst1, lst2):
	for e in lst2:
		lst1.append(e)
	return lst1