"""
Author: Yuxi Zhou
Start Date: 24-02-2022 17:49:17
"""

####------------------------------------------------####
#### Word Cloud Generator for Google Search Results ####
####------------------------------------------------####

## Importing the required packages ##

import google
from googlesearch import search
import urllib.request as url
from bs4 import BeautifulSoup
import re
import string
import pandas as pd
import nltk
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


opener = AppURLopener()
# response = opener.open('http://httpbin.org/user-agent')

# Fetching the search results for a Search Query (to be entered as user input) ##

qry = input("Enter search query: ")
search_results = search(query=qry, tld='com', lang='en', num=20, start=0, stop=20, pause=2.0)
urls = [s for s in search_results]

print(urls)
# Extracting the content from top 10 results ##

print("Extracting the content from top 10 search results..")
web_content_cleaned_all = []

for u in list(range(10)):
    weburl = opener.open(urls[u])
    web_content = weburl.read()
    print("content: ", web_content)
    web_content_cleaned = BeautifulSoup(web_content, "lxml").text
    web_content_cleaned = [val.lower() for val in web_content_cleaned.split(' ') if val.isalpha() or val.isnumeric()]
    web_content_cleaned_all.extend(web_content_cleaned)




# Cleaning the extracted content (lemmatization, stop word removal) ##

print("Processing the data..")
lemmatizer = WordNetLemmatizer()
qry_words = qry.lower().split(' ') + [lemmatizer.lemmatize(w) for w in qry.lower().split(' ')]
stop_words = list(set(stopwords.words('english'))) + qry_words + ['archived', 'original', 'retrieved']
web_content_cleaned_final = [lemmatizer.lemmatize(word) for word in web_content_cleaned_all if word not in stop_words]

## Generating the Word Cloud on cleaned text ##

print("Generating Word Cloud..")
text_final = ' '.join(web_content_cleaned_final)
wordcloud = WordCloud(max_font_size=100, max_words=500, background_color="rgba(255, 255, 255, 0)", mode="RGBA", random_state=0).generate(text_final)
plt.figure(figsize=(60, 50))
plt.imshow(wordcloud, interpolation="bilinear")
plt.title(qry + '\n', size=20)
plt.axis("off")
plt.savefig('poster01.png')
