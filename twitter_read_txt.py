#!/usr/bin/python3

import  tweepy
from textblob import  TextBlob
# creating  consumer key and secret key 
#  to authenticate twitter from ur accont 
consumer_key=''

consumer_secret=''

#  creating  access key and secret key 

access_key=''
access_secret=''


#  connecting for authenitcation 
#  here auth is very much similar to session variable  
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_key,access_secret)

#  connecting  API  
connect=tweepy.API(auth)

# now finding  data 
#print(dir(connect))
#                                number of tweets 
get_data=connect.search('trump',count=10)

#print(get_data)
#print(type(get_data))
# printing  data  
for i  in  get_data:
    analysis=TextBlob(i.text)
    print(analysis.sentiment)
