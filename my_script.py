
# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q=('#Polio OR #SPFx -filter:retweets'), lang='en').items(5):
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, q=('#Arduino OR #GIS OR #Python OR #EndPolio OR #Triathlon-filter:retweets'),lang='en').items(10):
            try:
                # Add \n escape character to print() to organize tweets
                print('\nTweet by: @' + tweet.user.screen_name)

                # Retweet tweets as they are found
                tweet.favorite()
                print('Like the tweet')

                sleep(5)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

