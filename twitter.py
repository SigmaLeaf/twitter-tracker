from twitterscraper import query_tweets
from flask import Flask
from flask import jsonify

app = Flask(__name__)

def getSearchJSON(keyword, multiplier):
	list_of_tweets = query_tweets(keyword, multiplier)
	a = []
	for tweet in list_of_tweets:
		e = {}
		e['user']		= tweet.user
		e['fullname']	= tweet.fullname
		e['id']			= tweet.id
		e['url']		= tweet.url
		e['timestamp']	= tweet.timestamp
		e['replies']	= tweet.replies
		e['likes']		= tweet.likes
		e['html']		= tweet.html
		a.append(e)
	d = {'tweets': a }
	return d

@app.route('/twitter/<search>')
def twitterSearch(search):
	return jsonify(getSearchJSON(str(search), 5))


if __name__ == "__main__":
	searches = ["Ethereum from:VitalikButerin", "Ethereum"]
	print(getSearchJSON(searches[0],20))

	app.run(threaded=True)

''' USEFUL DEBUG FUNCTIONS
def printDateTest(keyword, multiplier):
	for tweet in query_tweets(keyword, multiplier):
		print("timestamp: ", tweet.timestamp)


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
'''