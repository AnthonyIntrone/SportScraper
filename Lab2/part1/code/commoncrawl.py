#Adapted from News Please - https://github.com/fhamborg/news-please and http://automatingosint.com/blog/2015/08/osint-python-common-crawl/
#Authors: Anthony Introne
#         Michael Klein
import requests
from newsplease import NewsPlease
import json
import io
from urllib.error import HTTPError as HTTPERR
import gzip
import csv
from bs4 import BeautifulSoup


# Searches for the domain that is passed in
def search_domain(domain):
    record_list = []

    print("[*] Trying target domain: %s" % domain)

    for index in index_list:

        print("[*] Trying index %s" % index)

        cc_url = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&matchType=domain&output=json" % domain

        response = requests.get(cc_url)

        if response.status_code == 200:

            records = response.content.splitlines()

            for record in records:
                record_list.append(json.loads(record))

            print("[*] Added %d results." % len(records))

    print("[*] Found a total of %d hits." % len(record_list))

    return record_list

# Downloads a page with the given record
def download_page(record):
    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1

    prefix = 'https://aws-publicdatasets.s3.amazonaws.com/'

    resp = requests.get(prefix + record['filename'].decode('utf-8'), headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})

    raw_data = io.StringIO((resp.content).decode('utf-8'))
    f = gzip.GzipFile(fileobj=raw_data)

    data = f.read()

    response = ""

    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass

    return response

# Extraction of external links with html content and appending it to the link_list
def extract_external_links(html_content, link_list):
    parser = BeautifulSoup(html_content)
    links = parser.find_all("a")

    if links:
        for link in links:
            href = link.attrs.get("href")
            if href is not None:
                if 'espn.com' not in href:
                    if href not in link_list and href.startswith("http"):
                        print("[*] Discovered external link: %s" % href)
                        link_list.append(href)
    return link_list

#Search for articles from espn
record_list = search_domain('espn.com')
index_list = ["2019-04", "2019-09", "2019-13"]
ccNFL = []
ccESPORTS = []
ccNBA = []
ccNHL = []
ccNCAA = []
c = 0

#Create links with urlkey results
for link in record_list:
    if "30for30" not in link['urlkey'] and "2019" in link['timestamp']:
        if "esports" in link['urlkey'] and len(ccESPORTS)<100:
            ccESPORTS.append("https://www.espn.com/" + link['urlkey'][10:])
            c+=1
        elif "mens-college-basketball" in link['urlkey'] and len(ccNCAA)<100:
            ccNCAA.append("https://www.espn.com/" + link['urlkey'][10:])
            c+=1
        elif "nfl" in link['urlkey'] and len(ccNFL)<100:
            ccNFL.append("https://www.espn.com/" + link['urlkey'][10:])
            c+=1
        elif "nba" in link['urlkey'] and len(ccNBA)<100:
            ccNBA.append("https://www.espn.com/" + link['urlkey'][10:])
            c+=1
        elif "nhl" in link['urlkey'] and len(ccNHL)<100:
            ccNHL.append("https://www.espn.com/" + link['urlkey'][10:])
            c+=1
        if c == 500:
            break

#Writing urls
csvFile = io.open('../data/CommonCrawl/ccESPORTSlinks.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for url in ccESPORTS:
    csvWriter.writerow(''.join(url))
csvFile.close()

csvFile = io.open('../data/CommonCrawl/ccNFLlinks.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for url in ccNFL:
    csvWriter.writerow(''.join(url))
csvFile.close()

csvFile = io.open('../data/CommonCrawl/ccNHLlinks.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for url in ccNHL:
    csvWriter.writerow(''.join(url))
csvFile.close()

csvFile = io.open('../data/CommonCrawl/ccNBAlinks.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for url in ccNBA:
    csvWriter.writerow(''.join(url))
csvFile.close()

csvFile = io.open('../data/CommonCrawl/ccNCAAlinks.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for url in ccNCAA:
    csvWriter.writerow(''.join(url))
csvFile.close()

#Extract text files from links
txtFile = open('../data/CommonCrawl/ccESPORTSarticles.txt', 'a', encoding="utf-8")
for link in ccESPORTS:
    try:
        article = NewsPlease.from_url(link)
        if article.text is not None:
            txtFile.write(article.text)
    except HTTPERR:
        continue
txtFile.close()

txtFile = open('../data/CommonCrawl/ccNFLarticles.txt', 'a', encoding="utf-8")
for link in ccNFL:
    try:
        article = NewsPlease.from_url(link)
        if article.text is not None:
            txtFile.write(article.text)
    except HTTPERR:
        continue
txtFile.close()

txtFile = open('../data/CommonCrawl/ccNHLarticles.txt', 'a', encoding="utf-8")
for link in ccNHL:
    try:
        article = NewsPlease.from_url(link)
        if article.text is not None:
            txtFile.write(article.text)
    except HTTPERR:
        continue
txtFile.close()

txtFile = open('../data/CommonCrawl/ccNCAAarticles.txt', 'a', encoding="utf-8")
for link in ccNCAA:
    try:
        article = NewsPlease.from_url(link)
        if article.text is not None:
            txtFile.write(article.text)
    except HTTPERR:
        continue
txtFile.close()

txtFile = open('../data/CommonCrawl/ccNBAarticles.txt', 'a', encoding="utf-8")
for link in ccNBA:
    try:
        article = NewsPlease.from_url(link)
        if article.text is not None:
            txtFile.write(article.text)
    except HTTPERR:
        continue
txtFile.close()