from twitterscraper import query_tweets
from flask import Flask
from flask import jsonify
import datetime as dt

app = Flask(__name__)

""" CONST """
BEGIN_DATE = dt.date(2006,3,21)
MULTIPLIER = 1000

""" WRAPPERS """
def getSearchTodayJSON(keyword):
	"""
	Wrapper function to get a query of the search's tweets from today.
	"""
	today = dt.date.today() - dt.timedelta(days = 1)
	return getSearchJSON(keyword, MULTIPLIER, today)

def getCountTodayJSON(keyword):
	"""
	Wrapper function to get a count of the search's tweets from today.
	"""
	today = dt.date.today() - dt.timedelta(days = 1)
	return getCountJSON(keyword, MULTIPLIER, today)

def getSearchJSON(keyword, multiplier, begin=BEGIN_DATE):
	"""
	Returns a JSON of the query'd tweets from begin date to today.
	"""
	list_of_tweets = query_tweets(keyword, multiplier, begindate=begin)
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

def getCountJSON(keyword, multiplier, begin=BEGIN_DATE):
	"""
	Returns a JSON of the number of query'd tweets from begin date to today.
	"""
	list_of_tweets = query_tweets(keyword, multiplier, begindate=begin)
	return {"count": len(list_of_tweets)}

""" FLASK """
@app.route('/twitter-search/<search>')
def twitterSearch(search):
	return jsonify(getSearchTodayJSON(str(search)))

@app.route('/twitter-count/<search>')
def twitterCount(search):
	return jsonify(getCountTodayJSON(str(search)))

""" MAIN """
if __name__ == "__main__":
	app.run(threaded=True)f