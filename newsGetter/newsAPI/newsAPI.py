from newsapi import NewsApiClient
from newspaper import Article
from dotenv import load_dotenv
import os

load_dotenv()
newsapi = NewsApiClient(api_key=os.environ["NEWSAPI_KEY"])


def newsAPI():
    all_articles = newsapi.get_top_headlines(
        country="us",
        page=1,
    )

    all_articles = all_articles["articles"]
    formattedArticles = []
    for articles in all_articles:
        url = articles["url"]
        articleData = {
            "source": articles["source"],
            "author": articles["author"],
            "url": articles["url"],
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
