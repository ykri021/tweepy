import pandas as pd
import re

df = pd.read_csv('tweets.csv')
tweets = df['text']

replypattern = '^.*@.*'
urlpattern = '^.*https?.*'
hashpattern = '[^|¥s]#.*'

processedtweets = []

for tweet in tweets:
    i = re.sub(replypattern, '', str(tweet))
    i = re.sub(urlpattern, '', str(i))
    i = re.sub(hashpattern, '', str(i))
    if isinstance(i, str) and not i.split():
        pass
    else:
        processedtweets.append(i)

processedtweetsDataFrame = pd.Series(processedtweets)
newDF = pd.DataFrame({'text': processedtweetsDataFrame})

newDF.to_csv('processedtweets.csv')