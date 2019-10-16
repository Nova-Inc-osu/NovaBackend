import requests
url='http://127.0.0.1:8000/nova/conversations/1'
r = requests.get(url)
print(r)

import nltk # be sure to have stopwords installed for this using nltk.download_shell()
import pandas as pd
import string
messages = [line.rstrip() for line in open("profile.txt")]
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# install Vader and make sure you download the lexicon as well
sid = SentimentIntensityAnalyzer()
# this step will return an error if you have not installed the lexicon
summary = {"positive":0,"neutral":0,"negative":0}
for x in messages:
    ss = sid.polarity_scores(x)
    if ss["compound"] == 0.0:
        summary["neutral"] +=1
        print(x, ' - neutral')
    elif ss["compound"] > 0.0:
        summary["positive"] +=1
        print(x, ' - positive')
    else:
        summary["negative"] +=1
        print(x, ' - negative')
print(summary)