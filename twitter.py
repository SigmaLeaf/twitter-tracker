from twitterscraper import query_tweets

def printSimpleTest(keyword, multiplier):
	list_of_tweets = query_tweets(keyword, multiplier)

	for tweet in list_of_tweets:
		print("user: ", tweet.user)
		print("fullname: ", tweet.fullname)
		print("id: ", tweet.id)
		print("url: ", tweet.url)
		print("timestamp: ", tweet.timestamp)
		print("replies: ", tweet.replies)
		print("retweets: ", tweet.retweets)
		print("likes: ", tweet.likes)
		print("html: ", tweet.html)

def printDateTest(keyword, multiplier):
	for tweet in query_tweets(keyword, multiplier):
		print("timestamp: ", tweet.timestamp)

if __name__ == "__main__":
	searches = ["Ethereum from:VitalikButerin", "Ethereum"]
	printDateTest(searches[1], 100)

