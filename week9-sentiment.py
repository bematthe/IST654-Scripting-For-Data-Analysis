import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentences = ['This was a really good book.', 'This movie was so bad.',"I like to hate Michael Bay films, but I couldn't fault this one"]
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
	print(sentence)
	ss = sid.polarity_scores(sentence)
	for k in sorted(ss):
		print('{0}: {1}, '.format(k, ss[k]), end='')
	print()


