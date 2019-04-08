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

for l in script_lines:
    words = l.split(' ')
    name = []
    for w in words:
        w = w.strip()
        if w.isupper():
            name.append(w)
    if len(name) > 1:
        name = " ".join(name).replace(',', '')
        print (name)
