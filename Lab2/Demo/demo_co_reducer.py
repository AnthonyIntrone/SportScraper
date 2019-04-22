#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import re

current_word = None
current_count = 0
word = None

with open("mapper_output.txt","r") as nyt:
    with open("reducer_output.txt","w") as reducer:
        nytdata = nyt.readlines()
        for data in nytdata:
            # parse the input we got from mapper.py
            word = data[:len(data)-3]
            count = data[len(data)-2:len(data)-1]
    
            # convert count (currently a string) to int
            try:
                count = int(count)
            except ValueError:
                # count was not a number, so silently
                # ignore/discard this line
                continue

            # this IF-switch only works because Hadoop sorts map output
            # by key (here: word) before it is passed to the reducer
            if current_word == word:
                current_count += count
            else:
                if current_word:
                    # write result to STDOUT
                    reducer.write(current_word + str(current_count) + "\n")
                current_count = count
                current_word = word

        # do not forget to output the last word if needed!
        if current_word == word:
            reducer.write(current_word + str(current_count) + "\n")