import tweepy
import csv
import csvwriter
import pandas as pd
import collections

access_token = "852370042016727040-GjYU4WWt4wOw6FYEPqc084GvDncwMly"
access_token_secret = "n1xLvUmaafy7zMEfPSNSuLLuxKys4Gqb4LhwlaSJYc9Vy"
api_key ="JKk8xmWshf7v3HjbdIIOcReRs"
api_key_secret = "2a0RnTwkcVzku5xslbsdjYNXG8EyI0rqlJSTwQKB1drcAemuv7"

auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
fields = ['text']
filename = "gujrat_data_time.csv"
rows=[]
list = []
#to get tweet write particular hashtag
for tweet in tweepy.Cursor(api.search, q="#mumbaidiaries",
                   lang="en",
                   since="2018-01-01").items():
    ro = ["mumbai",tweet.text]
    rows.append(ro)
    print(ro)
with open('gujrat_data_time.csv', 'a', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
