import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs 

access_key = "y6y2COMi4fUESGC5On0oZHEFs"
access_secret = "VDrbjBAsbAMYUrt5oCVpScjXwlPacN6wg18LzVNrQRWW9QMs5d"
consumer_key = "1001803419399720960-PmbhUrBClMnG93rRyPZd5ekURwggQC"
consumer_secret = "lEb3eePGr6x2kctZzt631jRrzglxB3eYqP2lTuNfYvqi8"
 
# Authenticate using Twitter API v2 credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHXlygEAAAAAp%2BP2g44Qvl%2FzmPMjqwZvmcWEZmA%3D7xYExJ3sC94i2e7w2baZ3jf04rpfN9OUgmfgWyt36Z1D9Bp90I"

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