#!/usr/bin/env python

import sys

current_word = None
current_count = 0

# Input comes from stdin
for line in sys.stdin:
    word, count = line.strip().split(', ')
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Emit the word and its total count
            print(f"{current_word}, {current_count}")
        current_word = word
        current_count = count

# Don't forget to emit the last word if needed
if current_word:
    print(f"{current_word}, {current_count}")
