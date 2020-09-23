from tweepy import OAuthHandler , Stream
from tweepy.streaming import StreamListener
import tweepy
import json

ACCESS_TOKEN = '1016391********7232-**************Pr0jgOia61EKzzhU'
ACCESS_SECRET = 'TOCsx4wcfkmGKAoboU4***************4aWH26gi0x'
CONSUMER_KEY = 'LvZ4Xk**********GTFvMxxsG'
CONSUMER_SECRET = 'YMtDhvY51t6KNKCVOSCpz0y**********SX0SEWDB87ePoRB7K'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

for status in tweepy.Cursor(api.home_timeline).items(275):
    print(status._json)