#!/usr/bin/python
"""reducer.py"""

import sys

words = []

for line in sys.stdin:
    line = line.strip()
    if line not in words:
        words.append(line)

for i in words:
    print(i)

