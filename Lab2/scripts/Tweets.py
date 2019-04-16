import tweepy
import csv
import time
import io

#Setting twitter keys
api_key = "Pe4FZLCKXcchqgBFRpqQZtREl"
api_secret_key = "wsxTCKJSuGkEgN5cwaoAlYuHAyoIIVRbrKo8hG988MeWTUIyOG"
access_token = "1098665393076482048-OfIourBaN15zRQXORUL0zj8vx3e3JV"
access_token_secret = "luCeM1o01QocLc7RH7mWEg2F0dWZvrllbKQRXBkP7Tye3"

#Creating API objects
auth = tweepy.AppAuthHandler(api_key,api_secret_key)
api = tweepy.API(auth)

#sleeper
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except (tweepy.TweepError):
            print("Query limit reached, currently sleeping")
            time.sleep(15 * 60)
        except (StopIteration):
            break

buffer = 0

#NCAA tweets-1
csvFile = io.open('ncaa_tweets-1.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "march madness OR #marchmadness OR elite eight OR final four",lang = "en").items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer += 1
    if buffer == 5000:
        buffer = 0
        break
csvFile.close()

#NCAA tweets-2
csvFile = io.open('ncaa_tweets-1.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "sweet sixteen OR duke OR michigan state OR texas tech",lang = "en").items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer += 1
    if buffer == 5000:
        buffer = 0
        break
csvFile.close()

#NFL tweets
csvFile = io.open('nfl_tweets-1.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "nfl OR nfl draft OR mockdraft OR #nfldraft",lang = "en",).items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer += 1
    if buffer == 10000:
        buffer = 0
        break
csvFile.close()

#NBA tweets-1
csvFile = open('nba_tweets.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "nba OR nbaplayoffs OR lebron OR steph OR lakers OR warriors",lang = "en").items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer += 1
    if buffer == 5000:
        buffer = 0
        break
csvFile.close()

#NBA tweets-2
csvFile = open('nba_tweets.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "westbrook OR harden OR giannis OR draymond OR rockets",lang = "en").items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer += 1
    if buffer == 5000:
        buffer = 0
        break
csvFile.close()

#NHL tweets
csvFile = open('nhl_tweets.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "nhl OR nhlplayoffs",lang = "en").items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer += 1
    if buffer == 10000:
        buffer = 0
        break
csvFile.close()

#League tweets-1
csvFile = io.open('league_tweets.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "#lcs OR TSMWin OR FOXWin OR C9Win OR FLYWin OR GGSWin",lang = "en").items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer +=1
    if buffer == 5000:
        buffer = 0
        break
csvFile.close()

#League tweets-2
csvFile = io.open('league_tweets.csv', 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in limit_handled(tweepy.Cursor(api.search,q = "TLWin OR CGWin OR OPTWin OR 100Win OR CLGWin OR lolesports",lang = "en").items()):
    if 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.user.name, tweet.id_str, tweet.created_at, tweet.text])
        print(tweet.user.name, tweet.id_str, tweet.created_at, tweet.text)
        buffer += 1
    if buffer == 5000:
        buffer = 0
        break
csvFile.close()