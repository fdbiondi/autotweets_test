import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q=('#Cacerolazo OR #cacerolazo -filter:retweets'), lang='es').items(50):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
#         tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

