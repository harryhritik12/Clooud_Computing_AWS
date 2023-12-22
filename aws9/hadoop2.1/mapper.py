#!/usr/bin/python
import sys
import string

for line in sys.stdin:
    line = line.strip().lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        print(f"{word}\t1")
