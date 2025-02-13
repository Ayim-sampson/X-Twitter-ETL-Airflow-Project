import tweepy
import pandas as pd
from datetime import datetime

def run_x_etl():

    # Authenticate using Twitter API v2 credentials
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHXlygEAAAAAp%2BP2g44Qvl%2FzmPMjqwZvmcWEZmA%3D7xYExJ3sC94i2e7w2baZ3jf04rpfN9OUgmfgWyt36Z1D9Bp90I"

    client = tweepy.Client(bearer_token=bearer_token)

    # Fetch tweets from Elon Musk's timeline
    tweets = client.get_users_tweets(
        id="44196397",  # Elon Musk's user ID
        max_results=50,
        tweet_fields=["created_at", "public_metrics"]  # Request additional fields
    )

    # Print tweets
    if tweets.data:
        for tweet in tweets.data:
            print(f"{tweet.created_at}: {tweet.text}")
    else:
        print("No tweets found or access is restricted.")

    # Process tweets into a list of dictionaries
    tweet_list = []
    if tweets.data:
        for tweet in tweets.data:
            refined_tweet = {
                "user_id": tweet.author_id,  # API v2 does not return screen_name
                "text": tweet.text,
                "favorite_count": tweet.public_metrics["like_count"],
                "retweet_count": tweet.public_metrics["retweet_count"],
                "created_at": tweet.created_at
            }
            tweet_list.append(refined_tweet)

    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://ayim-airflow-project-bucket/elonmusk_twitter_data.csv", index=False)

    print("Twitter data saved successfully!")
