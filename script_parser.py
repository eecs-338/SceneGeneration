from fractions import Fraction
import re
import nltk
from nltk.corpus import stopwords
import numpy as np


script_lines = []
f = open("scene.txt", "r")
lines = f.readlines()
for l in lines:
    script_lines.append(str(l).strip())
    print (str(l).strip())


# add names to dict

name_dict = {}
for l in script_lines:
    words = l.split(' ')
    name = []
    if "EXT." not in l and "INT." not in l:
        for w in words:
            w = w.strip()
            if w.isupper():
                name.append(w)
        if len(name) > 1:
            name = " ".join(name).replace(',', ' ')
            # create dictionary of information
            name_dict[name] = {}
            print (name)


# valid people to talk ALL
