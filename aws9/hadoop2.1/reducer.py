#!/usr/bin/python
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip().split('\t')
    word, count = line[0], int(line[1])

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}")
        current_word = word
        current_count = count

# Print the result for the last word
if current_word:
    print(f"{current_word}")
