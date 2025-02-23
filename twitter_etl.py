import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs 
 
# Authenticate using Twitter API v2 credentials

# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="@elonmusk",
                           # 20 is the maximum allowed count
                           count=20,
                           include_rts = False,
                            # Necessary to keep full_text
                            # otherwise only the first 140 words are expected 
                            tweet_mode = 'extended'
                          )
print(tweets)