#!/usr/bin/env python
"""mapper.py"""

import sys

def ExtractAlphanumeric(InputString):
    from string import ascii_letters, digits
    return "".join([ch for ch in InputString if ch in (ascii_letters + digits)])

for line in sys.stdin:
    line = line.strip()
    line = line.replace(',', '')
    words = line.split()
    for word in words:
        word = ExtractAlphanumeric(word)
        word = word.lower()
        if len(word) != 0:
            print(f"{word}")
