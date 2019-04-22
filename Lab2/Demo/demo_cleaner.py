import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import io
import re
import csv
# Authors: Anthony Introne
#          Michael Klein
# Opening the files to read & write
orig_file = open("demo_text.txt", "r")
new_file = open("demo_clean.txt", "w")

# Defining stop words to extract from the text
stop_words = set(stopwords.words('english'))
charFilter = [':',':','"',',','.','/','?','<','>','!','@','#','$','%','^','&','*','(',')',')','_','•','-','—','1','2','3','4','5','6','7','8','9','0',
                'the','by','e','p']
for char in charFilter:
    stop_words.add(char)

# Grabbing all the text data and removing first step of stop words
all_text = []
for line in orig_file:
    for word in line.split():
        new_word = re.findall(r"^\w+", word.lower())
        if word not in stop_words:
            all_text.append(new_word)

# Removing digits
no_digits_text = []
for text in all_text:
    for string in text:
        if not string.isdigit():
            no_digits_text.append(string)

# Writing to file while removing remaining stop words
for string in no_digits_text:
    # for string in text:
    if string not in stop_words:
        new_file.write(string + "\n")    

orig_file.close()
new_file.close()
print("Demo Text is Cleaned")