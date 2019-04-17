# Authors: Anthony Introne
#          Mike Klein

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import io
import re
import pandas as pd
import csv

#        ________________________________________________________________________________
#       | NOTICE: BE IN THE Lab2/part1/code: directory before running the following code |
#       |________________________________________________________________________________|

# Cleaning the Twitter Data Collection
def cleanTwitterData(subtopic):

    all_text = []
    with open("../data/Twitter/" + subtopic + "_tweets.csv", 'r') as tweets:
        reader = csv.reader(, delimiter=',')
        for row in reader:
            all_text.append(row[1])
        
    print(all_text)
    text_column = data.iloc[:,3]
    text_column.to_csv(path_or_buf = "../data/Twitter/" + subtopic + "_data_text.csv", sep=' ', index=False, header=False)
    text = pd.read_csv("../data/Twitter/" + subtopic + "_data_text.csv")
    new_file = open("../data/Twitter/" + subtopic + "_data_clean.txt", "w")
    # for line in text:
    #     # print(line)
    #     new_file.write(line) 
    
    tweets.close()
    new_file.close()


    
# Cleaning the NYT Data Collection
def cleanNYTData(subtopic):

    # Opening the files to read & write
    orig_file = open("../data/NYT/" + subtopic + "_articles_text.txt", "r")
    new_file = open("../data/NYT/" + subtopic + "_data_clean.txt", "w")

    # Defining stop words to extract from the text
    stop_words = set(stopwords.words('english'))
    charFilter = [':',':','"',',','.','/','?','<','>','!','@','#','$','%','^','&','*','(',')',')','_','•','-','—','1','2','3','4','5','6','7','8','9','0',
                  'the','by','e']
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


# def cleanCCData(subtopic):





# *************************************** Main ***************************************

# cleanTwitterData("esports")
cleanTwitterData("nba")
# cleanTwitterData("nfl")
# cleanTwitterData("nhl")
# cleanTwitterData("ncaa")


# cleanNYTData("esports")
# cleanNYTData("nba")
# cleanNYTData("nfl")
# cleanNYTData("nhl")
# cleanNYTData("ncaam")

# cleanCCData("esports")
# cleanCCData("nba")
# cleanCCData("nfl")
# cleanCCData("nhl")
# cleanCCData("ncaam")
