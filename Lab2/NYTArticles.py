import json
import requests
from bs4 import BeautifulSoup


# *********************************************************************** E-Sports CODE ***********************************************************************
def grab_urls():
    urls = []
    for i in range(0,10):
        api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=e-sports&offset=" + str(i) + "&api-key=9vBbIBydobSjA6kGoUqq0MNGg4rqZtLy"
        data = requests.get(api_url)
        data = data.json()
        data = data['response']['docs']
        for url in data:
            urls.append(url['web_url'])
    return urls


def grab_text(url):
    
    session = requests.Session()
    req = session.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    paragraphs = soup.find_all('p')

    article = ""
    for p in paragraphs:
        article = article + p.get_text()
    return article

def process_data():
    league_articles = grab_urls()
    league_articles_text = ""
    for article in league_articles:
        league_articles_text = league_articles_text + grab_text(article)

    print(league_articles_text)
    
process_data()

# *********************************************************************** NHL Code ***********************************************************************