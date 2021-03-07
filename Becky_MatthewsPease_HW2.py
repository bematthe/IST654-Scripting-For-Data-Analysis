# -*- coding: utf-8 -*-
"""
#Becky Matthews-Pease
IST 652: Scripting for Data Analysis
Homework 2
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import tweepy as tw
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from twython import Twython
import advertools as adv


#Enter keys/tokens from Twitter Developer App 
auth_params = {
    'app_key': 'hK57n1i43E4Se3AnuPDgOOD8e',
    'app_secret': 'G4XthTYn0E4Zk3ZnfqRIHtWpZIrAxwVFAVWZlYXFwTzRqfEMsT',
    'oauth_token': '364289507-LkQJzbsnPNx5WnfAho4CfMIFaX7xoHqUZB3qq6lY',
    'oauth_token_secret': 'oe1fv2QptcuN6FscFs4fuTSmUCETWjUZVMJjFeT5Stexr',
}

#Load Twython module. These gather Tweets and return in a more organized format
twitter = Twython(**auth_params) 
adv.twitter.set_auth_params(**auth_params)

#Gathers tweets and users with the hashtag DisabilityTwitter
myTweets = adv.twitter.search(q='#DisabilityTwitter', count=900, tweet_mode='extended', lang='en')
#writes to a csv or json file; get column names
myTweets.to_csv('Becky_MatthewsPease_TweetOutput.csv', index=False)

#Pulls tweets back into python in a pandas data frame
df = pd.read_csv('C:/Users/becky/dts_tweets.csv', 
                     parse_dates=['tweet_created_at', 'user_created_at'])

#Get number of columns/rows, names of all columns
print(df.shape)
df.head(3)

#Show columns associated with the tweet vs. those for the author of the tweet
#User columns may have duplicated values
print('Columns starting with "tweet_" :', df.columns.str.contains('tweet_').sum()) 
print('Columns starting with "user_" :', df.columns.str.contains('user_').sum())

#Datetime attribute columns
df[['tweet_created_at', 'user_created_at']].dtypes

#Data Frame of User Data
dfUsers = pd.DataFrame(df[['user_screen_name', 'user_followers_count', 'user_description', 'user_created_at']])

#Top users with the most followers
topTen = dfUsers.sort_values(['user_followers_count'], ascending=False).head(10)

#Store top users and follower counts
data = {'debraruh':161572, 'AcademicChatter':124777, 'sallyephillips':72451,  
        'SFdirewolf':44957, 'DisVisibility':41889, 'mattbc':37467, 'MrSocial':37280, 'RebeccaCokley':33526} 
users = list(data.keys()) 
values = list(data.values()) 
   
#Plot Users with largest nummber of followers in bargraph
fig = plt.figure(figsize = (8, 5)) 
plt.xticks(rotation=45) 
# creating the bar plot 
plt.bar(users, values, color ='green',  
        width = 0.4) 
  
 
#Users with the most tweets in tag
df['user_screen_name'].value_counts().head(10)
#Store authors with the most tweets
data = {'CattranTanya':26, 'esioul':24, 'bennessb':13,  
        'ThisIsJordanKay':11, 'ConsciousBeing2':11, 'thejayfaulkner':6, 'DeathCab4Callie':5,  'markyready57':5, 'TheRealGrumpDad':5, 'm_e215':5,} 
users = list(data.keys()) 
values = list(data.values())
   #Plot users with the most tweets
fig = plt.figure(figsize = (10, 5)) 
plt.xticks(rotation=45) 
# creating the bar plot 
plt.bar(users, values, color ='green',  
        width = 0.4)               


#List the ways users are accessing twitter
print('Number of unique sources:', df['tweet_source'].nunique())
df['tweet_source'].value_counts().head(10)
#Store most frequent sources
data = {'Twitter for iPhone':309, 'Twitter for Android':268, 'Twitter Web App':255,  
        'Twitter for iPad ':26, 'TweetDeck':20, 'Buffer':12} 
sources = list(data.keys()) 
values = list(data.values())
#Plot the top ways users are accessing twitter:
fig = plt.figure(figsize = (6, 5)) 
plt.xticks(rotation=45) 
# creating the bar plot 
plt.bar(sources, values, color ='green',  
        width = 0.4)      


#List Tweets by day
tweet_df = df.groupby(pd.Grouper(key='tweet_created_at')).size()
#Store Tweets by day
data = {'Sunday':34, 'Saturday':181, 'Friday':255,  
        'Thursday':192, 'Wednesday':148, 'Tuesday':90} 
dates = list(data.keys()) 
values = list(data.values())
#Plot tweets by day
fig = plt.figure(figsize = (6, 5)) 
plt.xticks(rotation=45) 
# creating the bar plot 
plt.bar(dates, values, color ='green',  
        width = 0.4) 

########## Tweets in different formats ##########
#Tweets to DataFrame
dftweets = pd.DataFrame(df['tweet_full_text'])
#Tweets in list form
tweetlist = dftweets.values.tolist()
#Tweets as string
mytweets = pd.DataFrame.to_string(dftweets)


########## Tweet Content ##########

#Most commonly used words in Tweets
adv.word_frequency(text_list=df['tweet_full_text'], 
                   num_list=df['user_followers_count']).head(40)

#Average Freq of related words
(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('spoonie')
 .mean().round(3))

(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('inclusion')
 .mean().round(3))

(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('ADA')
 .mean().round(3))

(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('ADA')
 .mean().round(3))

(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('inaccessible')
 .mean().round(3))

(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('accommodations')
 .mean().round(3))

(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('advocacy')
 .mean().round(3))

(df['tweet_full_text']
 .drop_duplicates()
 .str.contains('ableism')
 .mean().round(3))


#Run sentiment analysis on text of tweets
def get_tweet_sentiment(mytweets): 
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(mytweets)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


# Create and generate a word cloud image:
wordcloud = WordCloud().generate(mytweets)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()






