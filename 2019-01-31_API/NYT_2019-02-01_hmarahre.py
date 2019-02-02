# WIM Python API workshop: 2019-02-01
# Helge Marahrens: hmarahre@iu.edu

# //- 1. read API documentation
# https://developer.nytimes.com/docs/archive-product/1/overview
# check the API limit
# 4000 requests per day
# 10 requests per minute

# //- 2. import packages
import requests
import json
import time
import pandas as pd
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# //- 3. authentication
# load NYT API key into Python
#path = ""
#local_file = path + 'NYT_auth.txt'
with open(local_file, "r") as txtfile:
    NYT_key = txtfile.read()

# //- 4. build get request
host = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
query = "?q=axolotl"
api_key = "&api-key=" + NYT_key
url = host + query + api_key

# //- 5. send get request – check server response
response = requests.get(url)
assert(response.status_code==200)
data = response.json()

# //- 6. explore data structures
data.keys()
data['status']
data['copyright']
type(data['response'])
data['response'].keys()
type(data['response']['docs'])
data['response']['meta']
len(data['response']['docs'])
data['response']['docs'][0].keys()
for i in range(len(data['response']['docs'])):
    print(data['response']['docs'][i]['headline']['main'])

# //- 7. save data
# create a dictionary
article_dict = defaultdict(list)
for i, article in enumerate(data['response']['docs']):
    article_dict[article['_id']] = [article['headline']['main'],\
#                          article['snippet'],\
                          article['pub_date'][0:4],\
                          article['word_count']]
    try:
        article_dict[article['_id']].append(article['news_desk'])
    except:
        article_dict[article['_id']].append("NA")

# create a dataframe
df = pd.DataFrame.from_dict(article_dict, orient='index')
df.columns = ['headline', 'year', 'word_count', 'news_desk']

# histogram of word count
plt.hist(df['word_count'])
plt.show()

## save as csv
#df.to_csv("NYT_articles.csv")
