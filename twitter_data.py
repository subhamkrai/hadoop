#!/usr/bin/python3

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time

analyzer = SentimentIntensityAnalyzer()

try:
	conn = sqlite3.connect('twitter.db')
	print("Connected successfully")
	c = conn.cursor()
except Exception as e:
	print(e)


def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()

#consumer key, consumer secret, access token, access secret.
ckey="6deFtYjAzmSApH9JI8vMNJl0f"
csecret="FQAFSw2wKXTo5UOTlO4vrX6ENwYK7RO34Tvg0iTGDchP7BVKFE"
atoken="2238047674-hcDqQMpGM30aJUsn0XBeyUYR2HqLES8VyaYzWlU"
asecret="3PYG0HEKQ9R6Z6TXQK4nhg7AZW8pLbngG9qbt8SslvwwZ"

class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)


while True:

    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["google"])
    except Exception as e:
        print(str(e))
        time.sleep(5)
