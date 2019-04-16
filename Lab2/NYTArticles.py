import json
import requests
from bs4 import BeautifulSoup
import csv
import io

# ****************************************************************** Multi-Purpose Functions ************************************************************

# Grabbing all the urls for a given sub topic in New York Times
def grab_article_urls(subtopic):
    urls = []
    for i in range(0,10):
        api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + subtopic + "&page=" + str(i) + "&api-key=9vBbIBydobSjA6kGoUqq0MNGg4rqZtLy"
        data = requests.get(api_url)
        data = data.json()
        data = data['response']['docs']
        for url in data:
            urls.append(url['web_url'])
    return urls

# Takes a url that will be used to grab its text through beautiful soup.
def grab_text(url):
    
    session = requests.Session()
    req = session.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ""
    for p in paragraphs:
        article_text = article_text + p.get_text()
    return article_text

# Takes the subtopic urls and gets all the text for each url by calling grab_esports_text()
def process_data(url_container, subtopic):
    articles_text = ""
    for url in url_container:
        articles_text = articles_text + grab_text(url)
    return articles_text

# ********************************************************************************************************************************************************
# ****************************************************************** ONLY RUN EACH CODE SECTION AT ONCE **************************************************
# *********************************************************************** UNCOMMENT/COMMENT OTHERS *******************************************************
# ********************************************************************************************************************************************************



# ********************************************************************* E-Sports Code ********************************************************************

# esports_text_file = open("esports_articles_text.txt", "w")
# esports_urls = grab_article_urls("e-sports")
# esports_text = process_data(esports_urls, "e-sports")
# esports_text_file.write(esports_text)
# esports_text_file.close()

# esports_urls_file = open("esports_articles_url.txt", "w")
# for url in esports_urls:
#     esports_urls_file.write(url)
# esports_urls_file.close()
# print("Finished Esports")

# *********************************************************************** NBA Code ***********************************************************************

# nba_text_file = open("nba_articles_text.txt", "w")
# nba_urls = grab_article_urls("nba")
# nba_text = process_data(nba_urls, "nba")
# nba_text_file.write(nba_text)
# nba_text_file.close()

# nba_urls_file = open("nba_articles_url.txt", "w")
# for url in nba_urls:
#     nba_urls_file.write(url)
# nba_urls_file.close()
# print("Finished NBA")

# *********************************************************************** NFL Code ***********************************************************************

# nfl_text_file = open("nfl_articles_text.txt", "w")
# nfl_urls = grab_article_urls("nfl")
# nfl_text = process_data(nfl_urls, "nfl")
# nfl_text_file.write(nfl_text)
# nfl_text_file.close()

# nfl_urls_file = open("nfl_articles_url.txt", "w")
# for url in nfl_urls:
#     nfl_urls_file.write(url)
# nfl_urls_file.close()
# print("Finished NFL")

# *********************************************************************** NHL Code ***********************************************************************

# nhl_text_file = open("nhl_articles_text.txt", "w")
# nhl_urls = grab_article_urls("nhl")
# nhl_text = process_data(nhl_urls, "nhl")
# nhl_text_file.write(nhl_text)
# nhl_text_file.close()

# nhl_urls_file = open("nhl_articles_url.txt", "w")
# for url in nhl_urls:
#     nhl_urls_file.write(url)
# nhl_urls_file.close()
# print("Finished NHL")

# ********************************************************************** NCAAM Code **********************************************************************

# ncaam_text_file = open("ncaam_articles_text.txt", "w")
# ncaam_urls = grab_article_urls("march madness")
# ncaam_text = process_data(ncaam_urls, "ncaam")
# ncaam_text_file.write(ncaam_text)
# ncaam_text_file.close()

# ncaam_urls_file = open("ncaam_articles_url.txt", "w")
# for url in ncaam_urls:
#     ncaam_urls_file.write(url)
# ncaam_urls_file.close()
# print("Finished NCAAM")