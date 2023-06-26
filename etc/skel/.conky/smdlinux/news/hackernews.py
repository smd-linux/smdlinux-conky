import feedparser

rss_url = "https://news.ycombinator.com/rss"
feed = feedparser.parse(rss_url)
count = len(feed['entries'])

for i in range(0, count):
	if i >= 10:
		break
	print(f"{feed.entries[i].title[0:100].encode('utf8')}"[1:])