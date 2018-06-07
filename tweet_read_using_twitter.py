#!/usr/lib/python3

try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
conumer_key ="BdTx7QVLk1UBqOfRqWm4IIIJS"
consumer_secret ="jWgFiEBOLBSyEIFeG7TuPEURVRoEbGYjz5pWgTCO1flZf7rg6C"
access_token ="2238047674-EUzXqARb7fVT4FHpSoERYu8OiGGgP1maB0Lb2zb"
access_token_secret ="rwI0bpKh2P6D2gzK01QMsKQt1JVmkRyQLl3YvRUhxjUzj"
 
oauth = OAuth(access_token, access_token_secret, conumer_key, consumer_secret )

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print (json.dumps(tweet))
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 
