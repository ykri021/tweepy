from __future__ import unicode_literals
import os
import sys
import io
import tweepy
from GenerateText import GenerateText
from tweet_listener import *



def tweets(api):

    generator = GenerateText(1)
    markovstring = generator.generate()
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=sys.stdout.encoding, errors="replace")
    print(markovstring)
    api.update_status(status=markovstring)


def twitter_bot():
    consumer_key = os.getenv("consumer_key")
    consumer_secret = os.getenv("consumer_secret")
    access_token = os.getenv("access_token")
    access_token_secret = os.getenv("access_token_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        tweets(api)
    except tweepy.TweepError as e:
        # duplicate status
        if e.api_code == 187:
            pass
        else:
            raise

if __name__ == '__main__':
    twitter_bot()
