import feedparser
import util

url = 'http://feeds.nos.nl/nosnieuwseconomie'
feed = feedparser.parse(url)

for entry in feed["entries"]:
 
	print(entry.title)
	util.create_wordcloud(entry.summary, entry.title)
	


