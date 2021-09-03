#need to install Tweepy, pandas, openpyxl for code to work

import tweepy
import pandas as pd
import Twitter_Credentials as cred

consumer_key = cred.consumer_key
consumer_secret = cred.consumer_secret
access_token = cred.access_token
access_token_secret = cred.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

number_of_tweets = 100
username = []
tweets = []
likes = []
time = []
retweets = []

cursor = tweepy.Cursor(api.search, q = ("(supermarket OR retail OR food OR grocery AND (Woolworths OR Woolies OR Australia)) -filter:retweets lang:en"), tweet_mode = "extended").items(number_of_tweets)

# cursor = tweepy.Cursor(api.user_timeline, id = "PhillyD", tweet_mode = "extended", exclude_replies = True, include_rts = False).items(number_of_tweets)

for tweet in cursor:
    username.append(tweet.user.screen_name)
    tweets.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)
    retweets.append(tweet.retweet_count)

df = pd.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})

df.to_excel("Twitter_Data.xlsx")
print(df)
