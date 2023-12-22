#/usr/bin/python
"""mapper.py"""
import sys
for line in sys.stdin:
    line=line.strip()
    words=line.split()
    for word in words:
        print('%s\t%s'%(word,1))


#!usr/bin/python
"""reducer.py"""

import sys
prev_word=None
prev_count=0
for line in sys.stdin:
    line=line.strip()
    words,count=line.split('\t')

    if(prev_word==word):
        prev_count+=count
    else:
        if prev_word:
            print('%s\t%s'%(prev_word,prev_count))
     