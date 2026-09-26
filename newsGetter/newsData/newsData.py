from newsdataapi import NewsDataApiClient
from newspaper import Article
from dotenv import load_dotenv
import os

load_dotenv()
api = NewsDataApiClient(apikey=os.environ["NEWSDATA_KEY"])


def newsData():
    response = api.news_api(country="us")["results"]

    formattedArticles = []
    for articles in response:
        url = articles["link"]
        articleData = {
            "source": articles["source_name"],
            "url": articles["link"],
            "title": articles["title"],
            "description": articles["description"],
            "content": None,
        }
        try:
            a = Article(url)
            a.download()
            a.parse()
            a.nlp()
            articleData["content"] = a.summary
        except Exception as e:
            print(f"Failed to get summary from: {url}\nError: {e}")

        formattedArticles.append(articleData)

    return formattedArticles
