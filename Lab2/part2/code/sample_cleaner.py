# Authors: Anthony Introne
#          Mike Klein

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import io
import re
import csv


def sample_cleaning():

    # Cleaning HFinn.txt
    with open("../sample_data/HFinn.txt", "r") as hfinn:
       hfinn_data = hfinn.readlines()

    hfinn_text = []
    for data in hfinn_data:
        hfinn_text.append(data.strip())
    
    
    clear_hfinn_text = []
    for string in hfinn_text:
        new_string = re.sub('[^\w\s]', '', string)
        if len(new_string) == 0:
            continue
        else:
            clear_hfinn_text.append(new_string)
    
    stop_words = set(stopwords.words('english'))
    charFilter = [':',':','"',',','.','/','?','<','>','!','@','#','$','%','^','&','*',
                  '(',')',')','_','•','-','—','1','2','3','4','5','6','7','8','9','0',
                  "the","by",'e',"and"]
    for char in charFilter:
        stop_words.add(char)
        
    clean_hfinn_text = []
    for text in clear_hfinn_text:
        if text not in stop_words:
            clean_hfinn_text.append(text)
    
    with open("../sample_data/HFinn_Clean.txt", "w") as hfinn_clean:
        for text in clean_hfinn_text:
            hfinn_clean.write(text)     
    

    hfinn.close()
    hfinn_clean.close()

    # Cleaning pg345.txt
    with open("../sample_data/pg345.txt", "r") as pg345:
        pg345_data = pg345.readlines()

    pg345_text = []
    for data in pg345_data:
        pg345_text.append(data.strip())
    
    
    clear_pg345_text = []
    for string in pg345_text:
        new_string = re.sub('[^\w\s]', '', string)
        if len(new_string) == 0:
            continue
        else:
            clear_pg345_text.append(new_string)

    clean_pg345_text = []
    for text in clear_pg345_text:
        if text not in stop_words:
            clean_pg345_text.append(text)

    with open("../sample_data/pg345_clean.txt", "w") as pg345_clean:
        for text in clean_pg345_text:
            pg345_clean.write(text)
    
    
    pg345.close()
    pg345_clean.close()

sample_cleaning()
