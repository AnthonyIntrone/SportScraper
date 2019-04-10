import json
import requests



def parse_articles():
    urls = []
    for i in range(0,10):
        
        api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=nba&offset=" + str(i) + "&api-key=9vBbIBydobSjA6kGoUqq0MNGg4rqZtLy"
        data = requests.get(api_url)
        data = data.json()
        data = data['response']['docs']
        for url in data:
            urls.append(url['web_url'])

    print(urls)
    return urls

league_articles = parse_articles()
