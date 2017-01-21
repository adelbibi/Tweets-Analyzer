import tweepy
import numpy as np
from textblob import TextBlob


consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret' 

access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve tweets
public_tweets = api.search('Trump',count=100)
polarities_all = []
with open('tweets.csv', 'wb') as csvfile:
		csvfile.write('tweet,sentiment value\n')
		for tweet in public_tweets:
			tweet_dummy1 = tweet.text
			tweet_edited = tweet_dummy1.replace(",", " ").replace("\n", " ")
			analysis = TextBlob(tweet_edited)
			polarities_all.append(analysis.sentiment[0])
			csvfile.write('%s, %f, \n' % (tweet_edited.encode('utf8'), analysis.sentiment[0]))
		
		print('Average sentiment values: ',np.mean(polarities_all))








# Extra cool functions
#print(tweets_to_analyze.sentiment.polarity) here(tweets_to_analyze is a textblob)
#api.update_status('tweepy + oauth!')
#user = api.get_user('adel_bibi') 
#print(user.screen_name)
#print(user.id)
#print(user.followers_count)
#print(api.get_status('822852037763284994'))
#api.get_user('231541858/AD_As3ad/screen_name')
#print(api.get_user('231541858/AD_As3ad/Ahmed Assad'))
