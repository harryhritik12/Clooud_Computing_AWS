#!/usr/bin/env python

import sys

# Input comes from stdin
for line in sys.stdin:
    # Split the line into words
    words = line.strip().split()
    for word in words:
        # Emit the word and a count of 1
        print(f"{word}, 1")
