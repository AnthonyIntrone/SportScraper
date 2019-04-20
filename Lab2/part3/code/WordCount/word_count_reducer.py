#!/usr/bin/env python
# reducer.py
import sys

# maps words to their counts
wordToCount = {} 

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert the count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        wordToCount[word] = wordToCount[word] + count
    except:
        wordToCount[word] = count

# write the tuples to stdout
# Note: they are unsorted (Let's sort them later)
for word in wordToCount.keys():
    print '%s\t%s' % (word, wordToCount[word])