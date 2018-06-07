# importing the module
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
 
# personal details
consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
data = trends1[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)


class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

for i in trendsName:
	twitter_stream.filter(track=[i])
