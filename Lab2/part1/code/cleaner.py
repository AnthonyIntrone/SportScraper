# Authors: Anthony Introne
#          Mike Klein

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import io
import re
import csv

#        ________________________________________________________________________________
#       | NOTICE: BE IN THE Lab2/part1/code: directory before running the following code |
#       |________________________________________________________________________________|

# Cleaning the Twitter Data Collection
def cleanTwitterData(subtopic):

    all_text = []
    with open("../data/Twitter/" + subtopic + "_tweets.csv", 'r') as tweets:
        reader = csv.reader(tweets, delimiter=',')
        for column in reader:
            if len(column) == 0:
                continue
            else:
                all_text.append(column[3])
    
    ready_text = []
    for text in all_text:
        list_text = text.split()
        for some_text in list_text:
            ready_text.append(some_text)

    clean_text = []
    for string in ready_text:
        if string[:4] == "http":
            continue
        else: 
            new_string = re.sub('[^\w\s]', '', string)
            if len(new_string) == 0:
                continue
            else:
                print(new_string)
            

    with open("../data/Twitter/" + subtopic + "_just_text.txt", "w") as tweets_text:
        for text in ready_text:
            tweets_text.write(text + "\n") 
    
    tweets.close()
    tweets_text.close()


    
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

cleanTwitterData("esports")
# cleanTwitterData("nba")
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
