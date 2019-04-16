import json
import requests
from bs4 import BeautifulSoup
import csv
import io
import time

# ****************************************************************** Multi-Purpose Functions ************************************************************

# Grabbing all the urls for a given sub topic in New York Times
def grab_article_urls(subtopic):
    urls = []
    for i in range(0,10):
        api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + subtopic + "&page=" + str(i) + "&sleep=10" + "&api-key=9vBbIBydobSjA6kGoUqq0MNGg4rqZtLy"
        data = requests.get(api_url)
        data = data.json()
        data = data['response']['docs']
        for url in data:
            urls.append(url['web_url'])
        time.sleep(7)
    return urls

# Takes a url that will be used to grab its text through beautiful soup.
def grab_text(url):
    
    session = requests.Session()
    req = session.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ""
    for p in paragraphs:
        article_text = article_text + "\n" + p.get_text()
    return article_text

# Takes the subtopic urls and gets all the text for each url by calling grab_esports_text()
def process_data(url_container, subtopic):
    articles_text = ""
    for url in url_container:
        articles_text = articles_text + grab_text(url)
    return articles_text

# Main function that calls all necessary functions and writes them to files for later use
def commander (subtopic, query):
    
    file_text_file = open(subtopic + "_articles_text.txt", "w")
    file_urls = grab_article_urls(query)
    file_text = process_data(file_urls, query)
    file_text_file.write(file_text)
    file_text_file.close()

    file_urls_file = open(subtopic + "_articles_url.txt", "w")
    for url in file_urls:
        file_urls_file.write(url + "\n")
    file_urls_file.close()
    print("Finished: " + query)


# Calling all subtopics with the designated query string

commander("esports", "e-sports")
commander("nba", "nba")
commander("nfl", "nfl")
commander("nhl", "nhl")
commander("ncaam", "march madness")