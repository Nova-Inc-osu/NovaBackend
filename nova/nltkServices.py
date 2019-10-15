# import requests
# graph_api_version = 'v2.9'
# # paste your access token below
# access_token = ' '
# # LHL's Facebook user id
# user_id = '125845680811480'
# # the id of LHL's response post at https://www.facebook.com/leehsienloong/posts/1505690826160285
# post_id = '1505690826160285'
# # the graph API endpoint for comments on LHL's post
# url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, user_id, post_id)
# comments = []
# r = requests.get(url, params={'access_token': access_token})
# while True:
#     data = r.json()
# # catch errors returned by the Graph API
#     if 'error' in data:
#         raise Exception(data['error']['message'])
# # append the text of each comment into the comments list
#     for comment in data['data']:
#         # remove line breaks in each comment
#         text = comment['message'].replace('\n', ' ')
#         comments.append(text)
# print('got {} comments'.format(len(data['data'])))
# # check if there are more comments
#     if 'paging' in data and 'next' in data['paging']:
#         r = requests.get(data['paging']['next'])
#     else:
#         break
# # save the comments to a file
# with open('comments.txt', 'w', encoding='utf-8') as f:
#     for comment in comments:
#         f.write(comment + '\n')

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