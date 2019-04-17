# Authors: Anthony Introne
#          Mike Klein

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import io
import re
import pandas as pd

#        ________________________________________________________________________________
#       | NOTICE: BE IN THE Lab2/part1/code: directory before running the following code |
#       |________________________________________________________________________________|

# Cleaning the Twitter Data Collection
def cleanTwitterData(subtopic):

    data = pd.read_csv("../data/Twitter/" + subtopic + "_tweets.csv")
    text_column = data.iloc[:,3]

    text_column.to_csv(path_or_buf = "../data/Twitter/" + subtopic + "_data_clean.csv", sep=' ', index=False, header=False)
    
# Cleaning the NYT Data Collection
def cleanNYTData(subtopic):

    # Opening the files to read & write
    orig_file = open("../data/NYT/" + subtopic + "_articles_text.txt", "r")
    new_file = open("../data/NYT/" + subtopic + "_data_clean.txt", "w")

    # Defining stop words to extract from the text
    stop_words = set(stopwords.words('english'))
    charFilter = [':',':','"',',','.','/','?','<','>','!','@','#','$','%','^','&','*','(',')',')','_','•','-','—','1','2','3','4','5','6','7','8','9','0']
    stringFilter = ["by"]
    for char in charFilter:
        stop_words.add(char)
    for string in stringFilter:
        stop_words.add(string)

    # Grabbing all the text data and removing all stop words
    all_text = []
    for line in original_file:
        for word in line.split():
            new_word = re.findall(r"^\w+", word.lower())
            if word not in stop_words:
                all_text.append(new_word)

    orig_file.close()
    # Writing to file
    for text in all_text:
        for string in text:
            print(string)
            new_file.write(string + "\n")
    new_file.close()


# def cleanCCData(subtopic):





# *************************************** Main ***************************************

# cleanTwitterData("esports")
cleanTwitterData("nba")
cleanTwitterData("nfl")
cleanTwitterData("nhl")
cleanTwitterData("ncaa")


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
