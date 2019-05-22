from fractions import Fraction
import re
## import nltk
## from nltk.corpus import stopwords
import numpy as np
import charData as cd


def createDict():
	name_dict = cd.newCharList()
	return name_dict
	
def promptNames(prompt, name_dict):
	words = prompt.split(' ')
	name = []
	
	for w in words: 	
		if w.isupper():
			name.append(w)
		else:
			if len(name) > 0:
				if len(name) == 1 and name[0] == 'I':
					1 + 1
				else:
					fname = " ".join(name).replace(',', '')
					if not cd.charMember(name_dict, fname):
						name_dict = cd.newChar(name_dict, fname)
			name = []
	return name_dict
				
				

def findNames(script_lines, name_dict):

	words = script_lines.split(' ')
	name = []

	for w in words: 	
		if w.isupper() or w == '\n':
			name.append(w)
		else:
			if len(name) > 0 and name[0] != '' and name[0] != "I":
				if len(name) > 2 and name[-1] == '\n' and name[0] == '\n':
					name = name[1:-1]
					fname = " ".join(name).replace(',', '')
					if fname[-8:] == "(CONT'D)":
						fname = fname[:-9]
					if len(fname) > 0 and fname[0] != '(':
						if len(fname) > 3 and fname[:3] != 'INT' and fname[:3] != 'EXT':
							fname = fname.strip()
							# create dictionary of information
							if not cd.charMember(name_dict, fname):
								name_dict = cd.newChar(name_dict, fname)
			name = []
	return name_dict
	