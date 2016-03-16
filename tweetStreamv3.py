import tweepy
from tweepy import Stream
from sys import exit
from http.client import IncompleteRead
# from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import re
import json
from keys import *
count = 0


#consumer key, consumer secret, access token, access secret.


class listener(StreamListener):

	def on_data(self, data):
		global count
		x = json.dumps(data)
		y = json.loads(data)
		print(y)
		#print(count)
		# printX()
		count = count + 1
		if count == 100000:
			exit(0)
		return (True)


	def on_error(self, status):
		print(status)


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

while True:
	try:
		twitterStream = tweepy.Stream(auth, listener())
		twitterStream.filter(track=["Election2016", "election2016", "GOP", "Republican", "Democratic", "Trump", "Donald", "Ted", "Cruz", "Marco", "Rubio", "Hillary", "Clinton", "Bernie", "Sanders", "Jeb", "Bush", "Ben", "Carson"])
	except IncompleteRead:
		continue